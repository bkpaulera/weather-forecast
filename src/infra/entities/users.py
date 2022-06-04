from sqlalchemy import Column, String, Integer
from src.infra.config.db_base import Base


class db_users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.name, self.email, self.password)
