import random
from typing import List
from database.sqlite_db import SQLiteDatabase
# from functools import lru_cache

class EncouragementService:
    def __init__(self, db: SQLiteDatabase, starter_encouragements: List[str]):
        self.db = db
        self.starter_encouragements = starter_encouragements

    def get_encouragements(self) -> List[str]:
        return self.db.get_encouragements() + self.starter_encouragements

    def add_encouragement(self, encouragement: str):
        current_list = self.get_encouragements()
        if encouragement in current_list:
            return
        self.db.add_encouragement(encouragement)

    def delete_encouragement(self, encouragement: str):
        current_list = self.get_encouragements()
        if encouragement not in current_list:
            return
        self.db.delete_encouragement(encouragement)

    def get_random_encouragement(self) -> str:
        return random.choice(self.get_encouragements())
