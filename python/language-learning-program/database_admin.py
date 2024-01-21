import csv
import sqlite3

def add_questions_manual(cursor: sqlite3.Cursor, table_name: str, data: list):
    '''Manually input 1 or more question data into the database.'''
    # Create the table if it doesn't exist
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY,
        word TEXT,
        category TEXT,
        answer TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT
        )
    ''')
    cursor.executemany(f'''
            INSERT INTO {table_name} (word, category, answer, option1, option2, option3)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', data)

def add_questions_csv(cursor: sqlite3.Cursor, table_name: str, csv_file: str):
    '''Add 1 or more question data from a csv file. The csv file has to match the columns from the SQLite database.'''
    # Create the table if it doesn't exist
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY,
        word TEXT,
        category TEXT,
        answer TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT
        )
    ''')
    with open(file=csv_file, mode='r', encoding="utf8") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            cursor.execute(f'''
                INSERT INTO {table_name} (word, category, answer, option1, option2, option3)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', row)

def add_listening_questions_csv(cursor: sqlite3.Cursor, table_name: str, csv_file: str):
    '''Add 1 or more question data from a csv file. The csv file has to match the columns from the SQLite database.'''
    # Create the table if it doesn't exist
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY,
        script TEXT,
        question TEXT,
        category TEXT,
        answer TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT
        )
    ''')
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            cursor.execute(f'''
                INSERT INTO {table_name} (script, question, category, answer, option1, option2, option3)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', row)

def delete_questions(cursor: sqlite3.Cursor, table_name: str, row_id: list):
    '''Delete one or more question data from the database.'''
    print(row_id)
    try:
        cursor.executemany(f"DELETE FROM {table_name} WHERE id=?", row_id)
    except sqlite3.OperationalError:
        print("table not found")

def update_question(cursor: sqlite3.Cursor, table_name: str, row_id: str, new_data: dict):
    '''Updates some values of a particular row from the database.'''
    datas = list(new_data.values())
    datas.append(row_id)
    columns = list(new_data.keys())
    prompt = [element + '=?' for element in columns]
    prompt = ','.join(prompt)
    cursor.execute(f'''
    UPDATE {table_name} 
    SET 
        {prompt}
    WHERE id=?
''', datas)

def gather_data_to_update(column: str) -> list:
    key_value = [column]
    user_choice = input(f'Update {column} data?\n1. Yes\n2. No\n > ')
    if user_choice == '1':
        key_value.append(input('Update to: '))
    elif user_choice == '2':
        key_value.append(False)
    return key_value

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

doing_admin_stuff = True

columns = ['word', 'category', 'answer', 'option1', 'option2', 'option3']
columns_listening = ['script', 'question', 'category', 'answer', 'option1', 'option2', 'option3']

while doing_admin_stuff:
    user_choice = input('Which table do you want to manage?\n1. vocabularies\n2. grammars\n3. listening\n4. Stop\n> ')
    if user_choice == '1':
        table_name = 'vocabularies'
    elif user_choice == '2':
        table_name = 'grammars'
    elif user_choice == '3':
        table_name = 'listening'
    elif user_choice == '4':
        doing_admin_stuff = False
        continue
    user_choice = input('Choose an action you want to do.\n1. Add data manually\n2. Add data from csv\n3. Delete data\n4. Update data\n> ')
    if user_choice == '1':
        if table_name == 'listening':
            print('Adding data manually...')
            compiling_data = True
            all_data = []
            while compiling_data:
                data = []
                data.append(input('question/word: '))
                data.append(input('category: '))
                data.append(input('answer: '))
                data.append(input('option1: '))
                data.append(input('option2: '))
                data.append(input('option3: '))
                all_data.append(data)
                user_choice = input("Add another data?\n1. Yes\n2. No\n> ")
                if user_choice == '2':
                    compiling_data = False
            add_questions_manual(cursor=cursor, table_name=table_name, data=all_data)
        else:
            print('Adding data manually...')
            compiling_data = True
            all_data = []
            while compiling_data:
                data = []
                data.append(input('question/word: '))
                data.append(input('category: '))
                data.append(input('answer: '))
                data.append(input('option1: '))
                data.append(input('option2: '))
                data.append(input('option3: '))
                all_data.append(data)
                user_choice = input("Add another data?\n1. Yes\n2. No\n> ")
                if user_choice == '2':
                    compiling_data = False
            add_questions_manual(cursor=cursor, table_name=table_name, data=all_data)
    elif user_choice == '2':
        if table_name == 'listening':
            print('Adding data from .csv file...')
            csv_file = input('Type in the csv file: ')
            if csv_file[-4:] != '.csv':
                csv_file = csv_file + '.csv'
            add_listening_questions_csv(cursor=cursor, table_name=table_name, csv_file=csv_file)
        else:
            print('Adding data from .csv file...')
            csv_file = input('Type in the csv file: ')
            if csv_file[-4:] != '.csv':
                csv_file = csv_file + '.csv'
            add_questions_csv(cursor=cursor, table_name=table_name, csv_file=csv_file)
    elif user_choice == '3':
        print('Deleting data...')
        row_ids = input('Type in the ids of rows you want to delete seperated by comma without space.\n> ')
        row_ids = row_ids.split(',')
        delete_questions(cursor=cursor, table_name=table_name, row_id=row_ids)
    elif user_choice == '4':
        print('Updating data...')
        updating = True
        while updating:
            row_id = input('Which id to update? ')
            new_data = {}
            for column in columns:
                one_data = gather_data_to_update(column)
                if one_data[1] != False:
                    new_data[one_data[0]] = one_data[1]
            update_question(cursor=cursor, table_name=table_name, row_id=row_id, new_data=new_data )
            user_choice = input('Update more data?\n1. Yes\n2. No\n>')
            if user_choice == '2':
                updating = False
            
#Commit the changes and close the connection
conn.commit()
conn.close()