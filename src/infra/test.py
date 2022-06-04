from config import *
from entities import *
BASE = db_connection_handler()
engine = BASE.get_db_engine()

print("Engine: ", engine[0])
print("Session: ", engine[1])
db_users.metadata.create_all(engine[0])


