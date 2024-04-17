from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a connection to the database
# "mysql+pymysql://username:password@host:port/database"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://u94nahquojoissoz:rgGRghcrOtLZpzed45Io@b6f2npw4xjvjnd9yveum-mysql.services.clever-cloud.com:3306/b6f2npw4xjvjnd9yveum"

# database motor
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Session generator
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base class
Base = declarative_base()
