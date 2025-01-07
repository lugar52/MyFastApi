from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MYSQLHOST:str="autorack.proxy.rlwy.net"
    MYSQLUSER:str="root"
    MYSQLPASSWORD:str="MoDBbSQWrEiOOPuetNOFxVQdeaLpwkWc"
    MYSQLDATABASE:str="railway"
    MYSQLPORT:str="45787"
    class Config:
        env_file = ".env.sample"


""" class Settings(BaseSettings):
    MYSQLHOST:str="localhost"
    MYSQLUSER:str="root"
    MYSQLPASSWORD:str="S2cr2t452"
    MYSQLDATABASE:str="railway"
    MYSQLPORT:str="3306"
    class Config:
        env_file = ".env.sample"
 """