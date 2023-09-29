import smtplib
from email.mime.text import MIMEText 
from flask import request, jsonify, session

class InvitacionController:
    
    @classmethod
    def enviar_invitacion(cls):
        # Configura los parámetros del servidor SMTP de tu proveedor de correo
        SMTP_SERVER = 'c0090432.ferozo.com'  # Cambia esto según tu proveedor de correo
        SMTP_PORT = 587  # Puerto SMTP TLS
        SMTP_USERNAME = 'discord@navarrosvending.com.ar'  # Tu dirección de correo
        SMTP_PASSWORD = 'Grupodeprueb@1'  # Tu contraseña de correo

        data = request.get_json()
        users = data.get("users")
        message = data.get("message")
        
        if not users or not message:
            return jsonify({'error': 'Datos faltantes'}), 400

        try:
            
            

            # Iniciar conexión SMTP
            smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            smtp.starttls()
            smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
            

            # Enviar correos electrónicos a los usuarios seleccionados
            for user in users:
                
                msg = MIMEText(message)
                msg['Subject'] = 'Invitación a nuestro servidor'
                msg['From'] = SMTP_USERNAME
                msg['To'] = user

                smtp.sendmail(SMTP_USERNAME, [user], msg.as_string())

            smtp.quit()

            return jsonify({'message': 'Invitaciones enviadas con éxito'}), 200
        # except Exception as e:
        except smtplib.SMTPException as e:
            print("Error al enviar el correo electrónico:", e)
            return jsonify({'error': 'Hubo un problema al enviar las invitaciones'}), 500
        
   
