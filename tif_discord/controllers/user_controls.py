from  ..models.user_models import User
from flask import Flask, request, jsonify, session
from ..models.errores_y_excepciones import DatoInvalido
class UserController:
    @classmethod
    def get_all(cls):
        users= User.get_all()
        users_list= []
        for user in users:
            users_list.append(user.serialize())
        return jsonify(users_list), 200
    
    @classmethod
    def get_one(cls, id_user):
        user= User(id_user=id_user)
        result= User.get_one(user)
        if result is not None:
            return jsonify(result.serialize()), 200
        
    @classmethod
    def create_user(cls):
        data= request.json
        user = User(**data)
        respuesta = User.create_user(user)
        if respuesta == True:
            return {"mensaje": "Usuario creado con exito"},201
        return respuesta
    
    @classmethod
    def update_user(cls):
        data= request.json
        data['id_user'] = session.get('id_user')
        user = User(**data)
        respuesta = User.update_user(user)
        if respuesta:
            return {"mensaje": "Usuario actualizado con exito"},200
        return {"mensaje": "dato duplicado"},404
    
    
    @classmethod
    def delete_user(cls, id_user):
        user= User(id_user=id_user)
        User.delete_user(user)
        return {"mensaje": "Usuario eliminado con exito"},204
    
    @classmethod
    def login(cls):
        data = request.json
        user = User(
            email = data.get('email'),
            password = data.get('password')
        )
        user = User.exist_user(user)
        if user:            
            session['id_user'] = user.id_user            
            return {"message": "Sesión iniciada"}, 200
        mensaje = "Correo electronico o contraseña incorrecto"
        raise DatoInvalido(description = mensaje, status_code= 401)
    
    @classmethod
    def logout(cls):
        session.clear()
        return {"message": "Sesión cerrada"}, 200
    
    @classmethod
    def get_session(cls):
        if (session.get('id_user')):
            id_user = session.get('id_user')
            result= User.get_session(id_user)
            if result is not None:
                return jsonify(result.serialize()), 200                
        return {'SESSION': 'NO hay session iniciada'}, 204

    @classmethod
    def show_profile(cls):
        id_user= session.get("id_user")
        user= User(id_user=id_user)
        result= User.get_one(user)
        if result is not None:
            return jsonify(result.serialize()), 200