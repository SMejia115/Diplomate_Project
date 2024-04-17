from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a connection to the database
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(
    user="uoz1kmogp2ocvaih",
    password="1dCU2QxR3AA7KDRcMdTy",
    host="bjytfnzaa8tm3pjxzswa-mysql.services.clever-cloud.com",
    port=3306,
    database="bjytfnzaa8tm3pjxzswa"
)

# database motor
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Session generator
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base class
Base = declarative_base()
