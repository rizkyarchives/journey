'''This Class will be in charge in dealing with users data in database as well as making a user instance
   Will be dealing with users and userCorrectAnswer tables in SQLite database.
'''
import bcrypt
import sqlite3
from datetime import datetime, date, timedelta
import pwinput
import requests
from random import choice

DATABASE_NAME = 'my_database.db'
USERS_TABLE_FORMAT = ('id', 'username', 'password_hash', 'real_name', 'created_at', 'last_login', 'streak', 'total_correct', 'total_attempted', 'last_streak_updated')
USERCORRECTANSWER_TABLE_FORMAT = ('id', 'userid', 'questionid', 'from_table', 'category')
DATA_POSITION = {key: value for (value, key) in enumerate(USERS_TABLE_FORMAT)}
DATE_FORMAT = "%d-%m-%Y"
TABLE_NAME = ['users', 'userCorrectAnswer']
API_KEY = 'u3M+UW2iExz08I2ZtYZRBQ==37ptn24g32TpEKSE'
QUOTE_CATEGORY = ['success', 'learning', 'education', 'courage', 'inspirational', None]
NEWS_API_KEY = "31d8c27b8f024871842283aff1580501" 
NEWS_ENDPOINT = 'https://newsapi.org/v2/top-headlines'

class User:
    def __init__(self, user_data: list):
        self.userid = user_data[DATA_POSITION['id']]
        self.username = user_data[DATA_POSITION['username']]
        self.password_hash = user_data[DATA_POSITION['password_hash']]
        self.real_name = user_data[DATA_POSITION['real_name']]
        self.created_at = user_data[DATA_POSITION['created_at']]
        self.previous_last_login = user_data[DATA_POSITION['last_login']]
        last_login = date.today()
        self.last_login = last_login.strftime(DATE_FORMAT)
        self.total_correct = user_data[DATA_POSITION['total_correct']]
        self.total_attempted = user_data[DATA_POSITION['total_attempted']]
        self.last_streak_updated = user_data[DATA_POSITION['last_streak_updated']]
        self.played_quiz_this_session = False
        self.streak = self.check_if_streak_valid(user_data[DATA_POSITION['streak']])
        self.update_users_table()
        self.quotes = self.get_quotes(choice(QUOTE_CATEGORY))
        self.article_link = self.get_link()
        self.progress_data = self.get_progress()

    def get_progress(self):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        from_table = ['vocabularies', 'grammars', 'listening']
        difficulties = ['easy', 'medium', 'hard']
        data = {}
        by_category = {}
        for table in from_table:
            cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME[1]} WHERE from_table=? AND userid=?", (table, self.userid,))
            total_by_type = cursor.fetchone()[0]
            by_category[table] = total_by_type
            if table != 'listening':
                by_difficulty = {}
                for difficulty in difficulties:
                    cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME[1]} WHERE from_table=? AND category=? AND userid=?", (table, difficulty, self.userid,))
                    total_by_category = cursor.fetchone()[0]
                    by_difficulty[difficulty] = total_by_category
                data[table] = by_difficulty
        data['total'] = by_category
        return data


    def get_link(self):
        params = {
    'country': 'us',
    'category': 'general',
    'apiKey': NEWS_API_KEY
}
        response = requests.get(NEWS_ENDPOINT, params=params)
        if response.status_code == requests.codes.ok:
            try:
                news = choice(response.json()['articles'])
                text = f'<a href="{news["url"]}">{news["title"]}</a>'
                return text
            except:
                return 'No article today.'
        else:
            return 'No article today.'

    def check_if_streak_valid(self, streak):
        last_login_object = datetime.strptime(self.last_login, DATE_FORMAT)
        last_streak_object = datetime.strptime(self.last_streak_updated, DATE_FORMAT)
        diff = last_login_object - last_streak_object
        date_difference = diff.days
        if date_difference > 1:
            last_streak_updated = last_login_object - timedelta(days=1)
            self.last_streak_updated = last_streak_updated.strftime(DATE_FORMAT)
            return 0
        else:
            return streak

    def insertTo_userCorrectAnswer_table(self, data: list):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        query = f"""
            INSERT INTO {TABLE_NAME[1]} {USERCORRECTANSWER_TABLE_FORMAT[1:]}
            VALUES ({','.join(['?' for _ in USERCORRECTANSWER_TABLE_FORMAT[1:]])})
            
        """
        cursor.executemany(query, data)

        conn.commit()
        conn.close()
        
    def update_users_table(self):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        query = [table_name + ' = ?' for table_name in USERS_TABLE_FORMAT[2:]]
        update_query = f"""
            UPDATE {TABLE_NAME[0]}
            SET
                {','.join(query)}
            WHERE username = ?
        """
        cursor.execute(update_query, self.format_userdata_to_list())

        conn.commit()
        conn.close()
    
    def update_attributes(self, new_data: dict):
        if self.check_if_streak_need_update():
            self.last_streak_updated = self.last_login
            self.streak = self.streak + 1
        self.total_attempted = self.total_attempted + new_data['total_attempted']
        self.total_correct = self.total_correct + len(new_data['correct_questions'])
        self.progress_data = self.get_progress()

    def check_if_streak_need_update(self):
        last_login_object = datetime.strptime(self.last_login, DATE_FORMAT)
        last_streak_object = datetime.strptime(self.last_streak_updated, DATE_FORMAT)
        diff = last_login_object - last_streak_object
        date_difference = diff.days
        if self.played_quiz_this_session and date_difference == 1:
            return True
        else:
            return False

    def format_userdata_to_list(self):
        return [self.password_hash, 
                self.real_name, 
                self.created_at, 
                self.last_login, 
                self.streak, 
                self.total_correct, 
                self.total_attempted,
                self.last_streak_updated,
                self.username]
    
    def get_userCorrectAnswer(self, **filters):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        columns = filters.keys()
        filter_query = [column +'=?' for column in columns]
        values = tuple(filters.values())
        cursor.execute(f"SELECT * FROM {TABLE_NAME[1]} WHERE {' AND '.join(filter_query)} ORDER BY RANDOM();", values)
        data = cursor.fetchall()

        conn.commit()
        conn.close()

        return data
    
    def get_quotes(self, category):
        import requests
        category = choice(QUOTE_CATEGORY)
        api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
        response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
        if response.status_code == requests.codes.ok:
            try:
                quote = f'"{response.json()[0]["quote"]}" -{response.json()[0]["author"]}'
                return quote
            except IndexError:
                return f'"You miss 100 percent of the shots you don\'t take" -EnglishMentor'
        else:
            return f'"You miss 100 percent of the shots you don\'t take" -EnglishMentor'

    @staticmethod
    def user_login_UI():
        username = input("username: ")
        password = pwinput.pwinput("password: ")
        return [username, password]

    @staticmethod
    def user_register_UI():
        typing_username = True
        while typing_username:
            username = input("username: ")
            user_exist = User.get_user_by_username(username=username)
            if user_exist:
                print("Username already exist!")
            else:
                typing_username = False
        password = pwinput.pwinput("password: ")
        real_name = input('real name: ')
        return [username, password, real_name] 
    
    @staticmethod
    def verify_credential(username: str, password: str):
        user_data = User.get_user_by_username(username=username)
        if user_data:
            verification_status = User.check_password(password=password, true_hash_password=user_data[2])
            if verification_status:
                return user_data
            else:
                return False
        else:
            return False
    
    @staticmethod
    def register_to_database(username: str, password: str, real_name: str):
        date_registered = date.today()
        date_registered_string = date_registered.strftime(DATE_FORMAT)
        password_hash = User.hash_password(password=password)
        new_user_data = tuple([username, password_hash, real_name, date_registered_string, date_registered_string, "0", "0", "0", date_registered_string])
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        query = f'''
            INSERT INTO {TABLE_NAME[0]} {tuple(USERS_TABLE_FORMAT[1:])}
            VALUES ({', '.join(['?' for _ in USERS_TABLE_FORMAT[1:]])})
        '''
        cursor.execute(query, new_user_data)

        conn.commit()
        conn.close()
 
    @staticmethod
    def get_user_by_username(username: str):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        user_data = cursor.fetchone()

        if user_data:
            conn.close()
            return user_data

        conn.close()
        return None
    
    @staticmethod
    def hash_password(password: str):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    @staticmethod
    def check_password(password: str, true_hash_password):
        return bcrypt.checkpw(password.encode('utf-8'), true_hash_password)