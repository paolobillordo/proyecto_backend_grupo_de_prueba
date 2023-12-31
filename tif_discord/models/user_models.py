from flask import jsonify
from ..database import DatabaseConnection
from mysql.connector import IntegrityError
from ..models.errores_y_excepciones import DatoInvalido

class User:
    # def __init__(self,**kwargs):
    #     self.id_user = kwargs.get('id_user', None)
    #     self.first_name = kwargs.get('first_name', None)
    #     self.last_name = kwargs.get('last_name', None)
    #     self.nick_name = kwargs.get('nick_name', None)
    #     self.email = kwargs.get('email', None)
    #     self.birth_date = kwargs.get('birth_date', None)
    #     self.password = kwargs.get('password', None)
    #     self.image = kwargs.get('image', None)

    def __init__(self,id_user = None, first_name = None, last_name = None, nick_name = None, email = None, birth_date = None, password = None, image = None):
        self.id_user= id_user
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.email = email
        self.birth_date = birth_date
        self.password = password
        self.image = image

    def serialize(self):
        return {
            "id_user": self.id_user,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "nick_name": self.nick_name,
            "email": self.email,
            "birth_date": self.birth_date,
            "password": self.password,
            "image": self.image
        }


    @classmethod
    def get_all(cls):
        query= """SELECT * FROM users """ #por si necesitamos todos los usuarios
        result= DatabaseConnection.fetch_all("railway", query)
        users= []
        if result is not None:
            for i in result:
                users.append(cls(*i))
        return users
    
    # @classmethod
    # def get_one(cls, user):
    #     query = """SELECT * FROM users WHERE id_user = %s """
    #     params = user.id_user,
    #     result = DatabaseConnection.fetch_one("railway", query, params)
    #     if result is not None:
    #         user_dict = {
    #             "id_user": result[0],
    #             "first_name": result[1],
    #             "last_name": result[2],
    #             "nick_name": result[3],
    #             "email": result[4],
    #             "birth_date": result[5],
    #             "password": result[6],
    #             "image": result[7]
    #         }
    #         return cls(**user_dict)
    #     return None
    
    
    
    @classmethod
    def get_one(cls, user):
        query= """SELECT * FROM users WHERE id_user = %s """ #obtiene 1 usuario por Id_user
        params= user.id_user,
        result= DatabaseConnection.fetch_one("railway", query, params)
        if result is not None:
            return cls(*result)
        return None # aca va un error
    
    @classmethod
    def create_user(cls, user):
        query= """INSERT INTO users (first_name, last_name, nick_name, email, birth_date, password, image) VALUE (%s,%s,%s,%s,%s,%s,%s)"""
        params= user.first_name, user.last_name, user.nick_name, user.email, user.birth_date, user.password,user.image
        try:
            DatabaseConnection.execute_query("railway", query, params)
            return True
        except IntegrityError as e: 
            mensaje_error = str(e)
            if "Duplicate entry" in mensaje_error:
                if "email" in mensaje_error:
                    mensaje = "El correo electrónico ya está en uso."
                elif "nick_name" in mensaje_error:
                    mensaje = "El nombre de usuario ya está en uso."
                else:
                    mensaje = "Error de duplicado en la base de datos."
            else:
                mensaje = "Error de integridad en la base de datos."

            raise DatoInvalido(description = mensaje)

    @classmethod
    def update_user(cls, user):
        claves = {"first_name", "last_name", "nick_name", "email", "birth_date", "password", "image"}
        query_parts = []
        params = []
        for key, values in user.__dict__.items():
            if key in claves and values is not None:
                query_parts.append(f"{key}=%s") 
                params.append(values)
        params.append(user.id_user)
        query = "UPDATE users SET " + ", ".join(query_parts) + " WHERE id_user = %s"
        try:
            DatabaseConnection.execute_query("railway", query, params)
            return True
        except Exception as e:
            return False 
    
    @classmethod
    def delete_user(cls, user):
        query= """DELETE FROM users WHERE id_user = %s"""
        params= user.id_user,
        DatabaseConnection.execute_query("railway", query, params)

    @classmethod
    def exist_user(cls, user):
        query= """SELECT * FROM users WHERE email = %s and password = %s"""
        params= (user.email, user.password)
        
        result= DatabaseConnection.fetch_one("railway", query, params)
        if result is not None:
            return cls(*result)
        return False

    @classmethod
    def get_session(cls, id_user):
        query= """SELECT * FROM users WHERE id_user = %s """
        params= id_user,
        result= DatabaseConnection.fetch_one("railway", query, params)
        if result is not None:
            return cls(*result)
        return None # aca va un error
