from flask import jsonify

class ExcepcionesPersonalizadas(Exception):
    def __init__(self, status_code, name = "Error Personalizado", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code


    def get_response(self):
            response = jsonify({
                'error': {
                    'code': self.status_code,
                    'name': self.name,
                    'description': self.description,
                }
            })
            response.status_code = self.status_code
            print(response.status_code)
            return response
 

class DatoInvalido(ExcepcionesPersonalizadas):
  def __init__(self, description = "Los datos ingresados no son válidos", name = "DatoInvalido", status_code = 400):
    super().__init__(status_code, name, description)
    


      