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
    def get_all(cls, id_channel):
        query = """SELECT * FROM messages WHERE id_channel = %s"""
        params = id_channel,
        result = DatabaseConnection.fetch_all("railway", query, params)
        messages = []
        if result is not None:
            for i in result:
                messages.append(cls(*i))
        return messages
    
    @classmethod
    def get_one(cls,message):
        query = "SELECT * FROM messages WHERE id_message = %s"
        params = message.id_message,
        result = DatabaseConnection.fetch_one("railway", query, params)
        if result is not None:
            return cls(*result)
        return None

#dedsde aca edite

    @classmethod
    def create_message(cls,message):
        query = """INSERT INTO messages (message, id_user, id_channel) VALUE (%s,%s,%s)"""
        params = message.message, message.id_user, message.id_channel
        DatabaseConnection.execute_query("railway", query, params)

    @classmethod
    def update_message(cls, message):
        claves = {"message", "id_user", "id_channel", "create_date"}
        query_parts = []
        params = []
        for key, values in message.__dict__.items():
            if key in claves and values is not None:
                query_parts.append(f"{key}=%s") 
                params.append(values)
        params.append(message.id_server)
        query = "UPDATE messages SET " + ", ".join(query_parts) + " WHERE id_message = %s"
        DatabaseConnection.execute_query("railway", query, params)

    @classmethod
    def delete_message(cls, message):
        query= """DELETE FROM messages WHERE id_message = %s"""
        params= message.id_message,
        DatabaseConnection.execute_query("railway", query, params)

    @classmethod
    def exist_user(cls, message):
        query= """SELECT * FROM servers WHERE id_message = %s"""
        params= message.id_message,
        result= DatabaseConnection.fetch_one("railway", query, params)
        if result is not None:
            return True
        return False

