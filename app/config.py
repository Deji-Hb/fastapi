from pydantic_settings import BaseSettings

#schema for env variables
class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        #filename where all personal info is stored
        env_file= ".env"

settings = Settings()
print(settings.database_username)