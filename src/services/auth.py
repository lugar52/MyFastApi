import os
from dotenv import load_dotenv
import jwt # used for encoding and decoding jwt tokens
import bcrypt

from fastapi import HTTPException # used to handle error handling
from passlib.context import CryptContext # used for hashing the password 
from datetime import datetime, timedelta # used to handle expiry time for tokens
import datetime

class Auth():
    hasher= CryptContext(schemes=['bcrypt'])
    load_dotenv()

    # Obtener la variable
    secret = os.getenv("APP_SECRET_STRING")

    # Verificar si se obtuvo correctamente
    if secret:
        print(f"Secreto cargado: {secret}")
    else:
        print("Error: APP_SECRET_STRING no está definido")

    def encode_password(self, password):
        return self.hasher.hash(password)

    def verify_password(self, password, encoded_password):
        return self.hasher.verify(password, encoded_password)
    
    def encode_token(self, username):
        print(datetime.datetime.now)
        print('misecret: ', self.secret)
        print(username)
        ahora = datetime.datetime.now(datetime.timezone.utc)  # Ahora en UTC con zona horaria
        expira = ahora + datetime.timedelta(minutes=30)  # Expira en X minutos

        payload = {
            'exp' : expira,
            'iat' : ahora,
            'sub' : username
        }
        print(payload)

        return jwt.encode(
            payload, 
            self.secret,
            algorithm='HS256'
        )
    
    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid token')
	    
    def refresh_token(self, expired_token):
        try:
            payload = jwt.decode(expired_token, self.secret, algorithms=['HS256'], options= {'verify_exp': False})
            username = payload['sub']
            new_token = self.encode_token(username)
            return {'token': new_token}
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid token')