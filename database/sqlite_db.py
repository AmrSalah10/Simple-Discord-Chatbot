import sqlite3
from typing import List

class SQLiteDatabase:
    def __init__(self, db_name: str):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        with self.connect() as db:
            cursor = db.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS encouragements (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    encouragement TEXT NOT NULL
                )
            ''')
            db.commit()

    def add_encouragement(self, encouragement: str):
        with self.connect() as db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO encouragements (encouragement) VALUES (?)', (encouragement,))
            db.commit()
            print(f'Added encouragement: {encouragement}')

    def get_encouragements(self) -> List[str]:
        with self.connect() as db:
            cursor = db.cursor()
            cursor.execute('SELECT encouragement FROM encouragements')
            return [row[0] for row in cursor.fetchall()]

    def delete_encouragement(self, encouragement: str):
        with self.connect() as db:
            cursor = db.cursor()
            cursor.execute('DELETE FROM encouragements WHERE encouragement = ?', (encouragement,))
            db.commit()
            print(f'Deleted encouragement: {encouragement}')
