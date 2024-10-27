class Database:
    def __init__(self) -> None:
        pass

"""
import psycopg2
from psycopg2 import sql
import random
from datetime import datetime

class Database:
    def __init__(self):
        # Параметры подключения к базе данных
        self.connection = psycopg2.connect(
            dbname="cinema",
            user="username",
            password="password",
            host="localhost",
            port="5432"
        )
        self.cursor = self.connection.cursor()
        print("Подключение к базе данных успешно установлено")

    def close(self):
        self.cursor.close()
        self.connection.close()
        print("Подключение к базе данных закрыто")

    def execute_query(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Запрос успешно выполнен")
        except Exception as e:
            print(f"Ошибка выполнения запроса: {e}")
            self.connection.rollback()

    def fetch_one(self, query, values=None):
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

# Пример использования
if __name__ == "__main__":
    db = Database()
    
    # Пример выполнения запроса
    query = "SELECT NOW();"
    result = db.fetch_one(query)
    print(f"Текущее время в базе данных: {result[0]}")

    # Закрытие подключения
    db.close()

"""