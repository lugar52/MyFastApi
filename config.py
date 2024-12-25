import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig():
    AMBI = 'development'
    #PORT="5432"
    DEBUG = True 
    #HOST = "34.168.253.122"
    HOST = "192.168.1.26"
    SECRET_KEY = os.getenv('SECRET_KEY')

config = {
    'development' : DevelopmentConfig 
}


