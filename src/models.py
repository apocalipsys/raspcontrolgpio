from src import db
from sqlalchemy import Column,String,Integer
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin



class Users(db.Model,UserMixin):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(20),unique=True)
    password_hash = Column(String(128))

    def __init__(self,username,password):
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)
