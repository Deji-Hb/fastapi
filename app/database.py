from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# this is the
# creates a session in the database for every request in the api endpoint and close it out when we're done
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


# #this is to connect to the postgresql database directly
# # incase i want to run raw SQL instead of using sqlalchemy
# while True:
#     try:
#         conn = psycopg2.connect(host = 'localhost', database ='fastapi', user = 'postgres',
#         password = 'deji0202', cursor_factory = RealDictCursor)
#         cursor = conn.cursor()
#         print("database connection was successful")
#         break
#     except Exception as error:
#         print("connecting to database failed")
#         print("error was", error)
#         time.sleep(2)
