from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:root@127.0.0.1:3306/db_py"

class db_connection_handler:

    def __init__(self):

        self.__db_connection = SQLALCHEMY_DATABASE_URI
        self.session = None

    def get_db_engine(self):
        engine = create_engine(self.__db_connection, echo=False)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        return engine, SessionLocal
