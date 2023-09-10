from flask import jsonify
from ..database import DatabaseConnection

class Servers:
    def __init__(self,id_server=None,name_server=None, description=None,id_user=None,icono=None):
        self.id_server = id_server
        self.name_server = name_server
        self.description = description
        self.id_user = id_user
        self.icono = icono

    def serialize(self):
        return {
            "id_server": self.id_server,
            "name_server": self.name_server,
            "description": self.description,
            "id_user": self.id_user,
            "icono": self.icono
        }
    
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM servers"""
        result = DatabaseConnection.fetch_all("discord_db", query)
        servers = []
        if result is not None:
            for i in result:
                servers.append(cls(*i))
        return servers
    
    @classmethod
    def get_one(cls,server):
        query = "SELECT * FROM servers WHERE id_server = %s"
        params = server.id_server,
        result = DatabaseConnection.fetch_one("discord_db", query, params)
        if result is not None:
            return cls(*result)
        return None # aca va un error
    
    @classmethod
    def create_server(cls,server):
        query = """INSERT INTO servers (name_server, description, id_user, icono) VALUE (%s,%s,%s,%s)"""
        params = server.name_server, server.description, server.id_user, server.icono
        DatabaseConnection.execute_query("discord_db", query, params)

    @classmethod
    def update_server(cls, server):
        claves = {"name_server", "description", "id_user", "icono"}
        query_parts = []
        params = []
        for key, values in server.__dict__.items():
            if key in claves and values is not None:
                query_parts.append(f"{key}=%s") 
                params.append(values)
        params.append(server.id_server)
        query = "UPDATE servers SET " + ", ".join(query_parts) + " WHERE id_server = %s"
        DatabaseConnection.execute_query("discord_db", query, params)

    @classmethod
    def delete_server(cls, server):
        query= """DELETE FROM servers WHERE id_server = %s"""
        params= server.id_server,
        DatabaseConnection.execute_query("discord_db", query, params)

    @classmethod
    def exist_user(cls, server):
        query= """SELECT * FROM servers WHERE id_server = %s"""
        params= server.id_server,
        result= DatabaseConnection.fetch_one("discord_db", query, params)
        if result is not None:
            return True
        return False

