from ..models.server_models import Servers  
from flask import request, jsonify, session

class ServerController:
    @classmethod
    def get_all(cls):
        servers= Servers.get_all() 
        servers_list= []
        for Server in servers:
            servers_list.append(Server.serialize())
        return jsonify(servers_list), 200

    @classmethod
    def get_servers_user(cls):
        id_user = session.get('id_user')
        servers= Servers.get_servers_user(id_user) 
        servers_list= []
        for Server in servers:
            session[Server.name_server] = Server.id_server
            servers_list.append(Server.serialize())
        return jsonify(servers_list), 200


    
    @classmethod
    def get_one(cls, id_server):
        server= Servers(id_server=id_server)
        result= Servers.get_one(server)
        if result is not None:
            return jsonify(result.serialize()), 200
        
    @classmethod
    def create_server(cls):
        data= request.json
        server = Servers(**data)
        Servers.create_server(server)
        return {"mensaje": "Servidor creado con exito"},201
    
    @classmethod
    def update_server(cls, id_server):
        data= request.json
        data['id_server'] = id_server
        server = Servers(**data)
        Servers.update_server(server)
        return {"mensaje": "Servidor actualizado con exito"},200
    
    @classmethod
    def delete_server(cls, id_server):
        server= Servers(id_server=id_server)
        Servers.delete_server(server)
        return {"mensaje": "Servidor eliminado con exito"},204