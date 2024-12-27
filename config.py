from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MYSQLHOST:str="autorack.proxy.rlwy.net"
    MYSQLUSER:str="root"
    MYSQLPASSWORD:str="MoDBbSQWrEiOOPuetNOFxVQdeaLpwkWc"
    MYSQLDATABASE:str="railway"
    MYSQLPORT:str="45787"
    class Config:
        env_file = ".env.sample"
