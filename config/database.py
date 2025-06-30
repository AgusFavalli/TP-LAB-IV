from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base


#Ingresar la ruta para conectar la DB despues de root:

DATABASE_URL = "mysql+mysqlconnector://root:0899JoseCandido@localhost:3306/alquiler"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()