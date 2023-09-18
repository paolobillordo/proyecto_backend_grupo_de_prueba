from ..models.message_models import Message  
from flask import request, jsonify, session

class MessageController:
    @classmethod
    def get_all(cls, id_channel):
        messages = Message.get_all(id_channel) 
        messages_list= []
        for message in messages:
            messages_list.append(message.serialize())
        return jsonify(messages_list), 200
    
    @classmethod
    def get_one(cls, id_message):
        message= Message(id_message=id_message)
        result= Message.get_one(message)
        if result is not None:
            return jsonify(result.serialize()), 200
    
    # desde aca empece a editar
    @classmethod
    def create_message(cls):
        data = request.json        
        data['id_user'] = session.get('id_user')
        print(data)
        mensaje = Message(**data)
        Message.create_message(mensaje)
        return {"mensaje": "Mensaje creado con exito"},201
    
    @classmethod
    def update_message(cls, id_message):
        data= request.json
        data['id_message'] = id_message
        message = Message(**data)
        Message.update_message(message)
        return {"mensaje": "Mensaje actualizado con exito"},200
    
    @classmethod
    def delete_message(cls, id_message):
        message= Message(id_message=id_message)
        Message.delete_message(message)
        return {"mensaje": "Mensaje eliminado con exito"},204
    