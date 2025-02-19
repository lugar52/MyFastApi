import json
from fastapi import FastAPI , Depends, APIRouter, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.database.connection import get_connection
from mysql.connector import MySQLConnection, Error

from src.services.auth import Auth
from src.models.user_modal import AuthModal

router = APIRouter(tags=["acceso"])

security = HTTPBearer()
auth_handler = Auth()

@router.post('/signup')
def signup(user_details: AuthModal, db: MySQLConnection = Depends(get_connection)):
    print('/signup')
    try:
        hashed_password = auth_handler.encode_password(user_details.password)
    
        cursor = db.cursor(dictionary=True)
        queryUpdate = ("""
            CALL railway.PROC_SIGNUP(%s, %s);
            """)
        values = (user_details.username, hashed_password)
        
        cursor.execute(queryUpdate, values)
        usuario = cursor.fetchall()
        cursor.close()
    
        if not usuario:
            raise HTTPException(status_code=404, detail="Result not found")

        if usuario and 'resultado' in usuario[0]:  
            valor = int(usuario[0]['resultado'] )

            if valor == -1: 
                return 'Error en el Insert'
            if valor == 0: 
                return 'Account already exists'
            if valor >= 1: 
                return {'IsSuccess': True, 'Usuario': user_details.username, 'pass' : hashed_password }

    except Error as err:
        print(f"Error: {err}")

    finally:
        db.close()

@router.post('/login')
def login(user_details: AuthModal, db: MySQLConnection = Depends(get_connection)):
    print('/login')
    print(user_details)
    try:
        cursor = db.cursor(dictionary=True)
        queryUpdate = ("""
            call PROC_SELECT_USER(%s);
            """)
        values = (user_details.username,)
        
        cursor.execute(queryUpdate, values)
        usuario = cursor.fetchall()
        cursor.close()
        user = usuario[0]['keyy']
        
        print(usuario[0]['password'])

        if user == '':
            return HTTPException(status_code=401, detail='Invalid username')
        
        if usuario[0]['password'] != '':
            if (not auth_handler.verify_password(user_details.password, usuario[0]['password'])):
                return HTTPException(status_code=401, detail='Invalid password')
            else:
                print(user)
                token = auth_handler.encode_token(user)
                return {'IsSuccess': True, 'token': token}
            
    except Error as err:
        print(f"Error: {err}")

    finally:
        db.close()

@router.get('/refresh_token')
def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    expired_token = credentials.credentials
    return auth_handler.refresh_token(expired_token)

@router.post('/secret')
def secret_data(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    if(auth_handler.decode_token(token)):
        return 'Top Secret data only authorized users can access this info'

@router.get('/notsecret')
def not_secret_data():
    return 'Not secret data'