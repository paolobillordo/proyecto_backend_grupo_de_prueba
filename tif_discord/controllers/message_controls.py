from ..models.message_models import Message  
from flask import request, jsonify

class MessageController:
    @classmethod
    def get_all(cls):
        messages= Message.get_all() 
        messages_list= []
        for message in messages:
            messages_list.append(message.serialize())
        return jsonify(messages_list), 200
    