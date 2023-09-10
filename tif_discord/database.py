# hace falta in stalar: pip install python-decouple para poder usar .env
from decouple import config
import mysql.connector 
class DatabaseConnection: 
    _connection = {} 

    @classmethod
    def get_connection(cls, name_base):
        if name_base not in cls._connection:
            cls._connection[name_base] = mysql.connector.connect(
                host=config("DATABASE_HOST"),
                user=config("DATABASE_USERNAME"),
                port=config("DATABASE_PORT"),
                password=config("DATABASE_PASSWORD"),
                database=name_base
            )
        return cls._connection[name_base]

    @classmethod
    def execute_query(cls, name_base, query, params=None):
        try:
            cursor = cls.get_connection(name_base).cursor()
            cursor.execute(query, params)
            cls._connection[name_base].commit()
            return cursor
        finally:
            cls.close_connection(name_base)

    @classmethod
    def fetch_one(cls, name_base, query, params=None):
        try:
            cursor = cls.get_connection(name_base).cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
        finally:
            cls.close_connection(name_base)

    @classmethod
    def fetch_all(cls, name_base, query, params=None):
        try:
            cursor = cls.get_connection(name_base).cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        finally:
            cls.close_connection(name_base)

    @classmethod 
    def close_connection(cls, name_base): 
        if name_base in cls._connection:
            cls._connection[name_base].close()
            del cls._connection[name_base]
