import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


class Datanbase:
    def __init__(self, db_host, db_name, db_username, db_password):
        self.conn = psycopg2.connect(
            host=os.getenv("db_host"),
            database=os.getenv("db_name"),
            user=os.getenv("db_username"),
            password=os.getenv("db_password"),
        )
        self.cursor = self.conn.cursor()

    def fetch(self, query: str):
        self.cursor.execute(query=query)
        return self.cursor.fetchall()

    def execute(self, query: str):
        self.cursor.execute(query)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
