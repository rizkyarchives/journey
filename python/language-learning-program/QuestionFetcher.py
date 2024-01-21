'''This Class will be in charge in taking questions data from the database
   Will have access to vocabularies, grammars, and listening tables in SQLite database.
'''
import sqlite3
import random

QUESTION_TABLE_COLUMNS = ['id', 'question', 'category', 'answer', 'option1', 'option2', 'option3']
LISTENING_QUESTION_TABLE_COLUMNS = ['id', 'script', 'question', 'category', 'answer', 'option1', 'option2', 'option3']

class QuestionsHandler():
    def __init__(self, db_name: str, *table_names):
        self.file = db_name
        self.tables = list(table_names)
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def fetch_questions_byCategory(self, table_name: str, category: str):
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE category=? ORDER BY RANDOM()", (category,))
        data = self.cursor.fetchall()
        return self.format_question_data_to_dict(QUESTION_TABLE_COLUMNS, data)
    
    def fetch_listening_questions_byCategory(self, table_name: str, category: str):
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE category=? ORDER BY RANDOM()", (category,))
        data = self.cursor.fetchall()
        return self.format_listening_question_data_to_dict(LISTENING_QUESTION_TABLE_COLUMNS, data)
    
    def fetch_all_listening_questions(self, table_name: str):
        self.cursor.execute(f"SELECT * FROM {table_name} ORDER BY RANDOM()", ())
        data = self.cursor.fetchall()
        return self.format_listening_question_data_to_dict(LISTENING_QUESTION_TABLE_COLUMNS, data)
    
    def fetch_all_questions(self, table_name: str):
        self.cursor.execute(f"SELECT * FROM {table_name} ORDER BY RANDOM()", ())
        data = self.cursor.fetchall()
        return self.format_question_data_to_dict(QUESTION_TABLE_COLUMNS, data)

    def count_questions(self):
        # Count all data
        compiled_count_data = {}
        total_questions_per_table = {}
        category_counts = []
        for table in self.tables:
            self.cursor.execute(f"SELECT COUNT(*) FROM {table}")
            total_questions_per_table[table] = self.cursor.fetchone()[0]
            self.cursor.execute(f"SELECT category, COUNT(*) FROM {table} GROUP BY category")
            category_counts = {category: total for (category, total) in self.cursor.fetchall()}
            compiled_count_data[table] = category_counts
        compiled_count_data['total'] = total_questions_per_table
        return compiled_count_data
    
    def format_question_data_to_dict(self, columns: list, data: list):
        result = []
        for element in data:
            data_in_dict = dict(zip(columns[:4], element[:4]))
            options = element[3:]
            data_in_dict['options'] = options
            data_in_dict['options'] = list(data_in_dict['options'])
            random.shuffle(data_in_dict['options'])
            data_in_dict['options'] = tuple(data_in_dict['options'])
            result.append(data_in_dict)
        return result
    
    def format_listening_question_data_to_dict(self, columns: list, data: list):
        result = []
        for element in data:
            data_in_dict = dict(zip(columns[:5], element[:5]))
            options = element[4:]
            data_in_dict['options'] = options
            data_in_dict['options'] = list(data_in_dict['options'])
            random.shuffle(data_in_dict['options'])
            data_in_dict['options'] = tuple(data_in_dict['options'])
            result.append(data_in_dict)
        return result