import mysql.connector


class Database:
    def __init__(self):
        pass

    @staticmethod
    def connector():
        return mysql.connector.connect(
            host="",
            database="",
            user="",
            password=""
        )