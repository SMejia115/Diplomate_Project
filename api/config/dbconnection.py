from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a connection to the database
# "mysql+pymysql://username:password@host:port/database"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:I$aacPachon33@localhost:3306/capclock"

# database motor
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Session generator
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base class
Base = declarative_base()
