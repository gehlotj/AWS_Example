from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, MetaData, Table, String
from sqlalchemy.orm import sessionmaker,scoped_session, create_session

from flask_jwt_extended import (JWTManager, jwt_required,
                                jwt_refresh_token_required,
                                jwt_optional, fresh_jwt_required,
                                get_raw_jwt, get_jwt_identity,
                                create_access_token, create_refresh_token,
                                set_access_cookies, set_refresh_cookies,
                                unset_jwt_cookies,unset_access_cookies)

#setting up database
db = SQLAlchemy()
engine = None
db_session = scoped_session(lambda: create_session(autocommit = False, autoflush=False,bind=engine))

#setting up jwt
jwt_manager = JWTManager()

#db table
class Users(db.Model):
    __tablename__ = 'USR'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

class Stu(db.Model):
    __tablename__ = "STU"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    grade = Column(Integer)


class Database:
    def init_engine(configValue):
        global engine
        engine = create_engine(configValue)
        return engine
