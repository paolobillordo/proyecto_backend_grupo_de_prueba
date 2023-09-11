from flask import jsonify
from ..database import DatabaseConnection

class Message:
    def __init__(self, id_message=None, message=None, id_user= None, id_channel=None, create_date=None):
        self.id_message = id_message
        self.message = message
        self.id_user = id_user
        self.id_channel = id_channel
        self.create_date = create_date

    
    def serialize(self):
        return {
            "id_message": self.id_message,
            "message": self.message,
            "id_user": self.id_user,
            "id_channel": self.id_channel,
            "create_date": self.create_date  # Convertir a cadena si es necesario
        }
    
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM messages"""
        result = DatabaseConnection.fetch_all("discord_db", query)
        messages = []
        if result is not None:
            for i in result:
                messages.append(cls(*i))
        return messages
