from ..models.channel_model import Channel
from flask import request, jsonify, session

class ChannelController:
    @classmethod
    def get_all(cls, name_server):           
        id_server = session.get(name_server)
        channels= Channel.get_all(id_server)
        channels_list= []
        for channel in channels:
            channels_list.append(channel.serialize())
        return jsonify(channels_list), 200
    
    @classmethod
    def get_one(cls, id_channel):
        channel= Channel(id_channel=id_channel)
        result= Channel.get_one(channel)
        if result is not None:
            return jsonify(result.serialize()), 200
    
    @classmethod
    def create_channel(cls):
        data = request.json
        data['id_user'] = session.get('id_user')
        channel = Channel(**data)
        Channel.create_channel(channel)
        return {"mensaje": "Canal creado con exito"},201
    
    @classmethod
    def update_channel(cls, id_channel):
        data= request.json
        data['id_channel'] = id_channel
        channel = Channel(**data)
        Channel.update_channel(channel)
        return {"mensaje": "Canal modificado con exito"},200
    
    @classmethod
    def delete_channel(cls, id_channel):
        channel= Channel(id_channel=id_channel)
        Channel.delete_channel(channel)
        return {"mensaje": "Canal eliminado con exito"},204
        