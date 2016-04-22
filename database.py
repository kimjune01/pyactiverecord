import mysql.connector
import json


class Database:
    def __init__(self):
        pass

    @staticmethod
    def connector():
        obj = json.loads(open('config.json', 'r').read())
        return mysql.connector.connect(
            host=obj["host"],
            database=obj["database"],
            user=obj["user"],
            password=obj["password"]
        )