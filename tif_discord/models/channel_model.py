from flask import jsonify
from ..database import DatabaseConnection

class Channel:
    def __init__(self,id_channel = None, name_channel = None, description = None, id_server = None, id_user = None, create_date = None):
        self.id_channel = id_channel
        self.name_channel = name_channel
        self.description = description
        self.id_server = id_server
        self.id_user = id_user
        self.create_date = create_date
        
    def serialize(self):
        return {
            "id_channel": self.id_channel,
            "name_channel": self.name_channel,
            "description": self.description,
            "id_server": self.id_server,
            "id_user": self.id_user,
            "create_date": self.create_date
        }
    
    @classmethod
    def get_all(cls, id_server):
        query = """SELECT * FROM channels WHERE id_server = %s"""
        params = id_server,
        result = DatabaseConnection.fetch_all("railway", query, params)
        channels = []
        if result is not None:
            for i in result:
                channels.append(cls(*i))
        return channels
    
    @classmethod
    def get_one(cls, id_channel):
        query = """SELECT * FROM channels WHERE id_channel = %s"""
        params = (id_channel,)
        result = DatabaseConnection.fetch_one("railway", query, params)
        if result is not None:
            return cls(*result)
        return None
    
    @classmethod
    def create_channel(cls, channel):
        query = """INSERT INTO channels (name_channel, description, id_server, id_user, create_date) VALUES (%s, %s, %s, %s, %s)"""
        params = (channel.name_channel, channel.description, channel.id_server, channel.id_user, channel.create_date)
        DatabaseConnection.execute_query("railway", query, params)

    @classmethod
    def update_channel(cls, channel):
        claves = {"name_channel", "description", "id_server", "id_user", "create_date"}
        query_parts = []
        params = []
        for key, values in channel.__dict__.items():
            if key in claves:
                query_parts.append(f"{key}=%s") 
                params.append(values)
        params.append(channel.id_channel)
        query = f"UPDATE channels SET {','.join(query_parts)} WHERE id_channel = %s"
        DatabaseConnection.execute_query("railway", query, params)

    @classmethod
    def delete_channel(cls, channel):
        query= """DELETE FROM channels WHERE id_channel = %s"""
        params = (channel.id_channel,)
        DatabaseConnection.execute_query("railway", query, params)
        
    @classmethod
    def exist_channel(cls, channel):
        query= """SELECT * FROM channels WHERE id_channel = %s"""
        params = (channel.id_channel,)
        result = DatabaseConnection.fetch_one("railway", query, params)
        if result is not None:
            return True
        return False
       