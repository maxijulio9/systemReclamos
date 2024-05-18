import sys
import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select
from config_vars import BBDD_CONNECTION


Base = declarative_base()

class Estado(Base):
    __tablename__ =  "estado"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    metadata = MetaData()
    estado = Table("estado", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    
    @classmethod
    def parameters_by_id(cls, *, est_id):
        """
        Cuáles son los parámetros
        """
        query = select([cls.estado]).where(cls.estado.c.est_id == est_id)
        return cls.connection.execute(query).fetchall()


    @classmethod
    def all_status(cls):
        """
        Cuáles son las categorias (en caso de no pasar parámetros)
        """
        query = select([cls.estado])
        return query
        
    @classmethod
    def single_status(cls, est_id):
        """
        Cuáles son las estado(solo nombre) con el est_id
        """
        query = select([cls.estado]).where(cls.estado.c.est_id == est_id)
        return query
    
    @classmethod
    def single_status_by_name(cls,est_nombre):
        """
        Cuáles son las status con el est_nombre igual
        """
        query = select([cls.estado]).where(cls.estado.c.est_nombre == est_nombre)
        return query
