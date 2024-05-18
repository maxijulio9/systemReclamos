
import sys
import os
dirname = os.path.dirname(__file__)
 
sys.path.append(dirname)
sys.path.append(dirname+"/db_models/")

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select,join
from config_vars import BBDD_CONNECTION

from db_models import municipio

Base = declarative_base()

class Provincia(Base):
    
    __tablename__ =  "PROVINCIA"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    connection = engine.connect()
    metadata = MetaData()
    provincia = Table("PROVINCIA", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    
    @classmethod
    def parameters_by_id(cls, *, prov_id):
        """
        Cuáles son los parámetros
        """
        query = select([cls.provincia]).where(cls.provincia.c.prov_id == prov_id)
        return cls.connection.execute(query).fetchall()

    @classmethod
    def all_provinces(cls):
        """
        Cuáles son las provincias (en caso de no pasar parámetros)
        """
        query = select([cls.provincia])
        return query

    @classmethod
    def single_province(cls, *, prov_id):
        """
        Cuáles son las provincias con el prov_id
        """
        query = select([cls.provincia]).where(cls.provincia.c.prov_id == prov_id)
        return query
    
    @classmethod
    def single_provincia_by_name(cls, *, prov_nombre):
        """
        Cuáles son las provincia con el prov_nombre igual
        """
        query = select([cls.provincia]).where(cls.provincia.c.prov_nombre == prov_nombre)
        return query
        
    @classmethod
    def single_provincia_by_address(cls, *, prov_direccion):
        """
        Cuáles son las provincia con el prov_nombre igual
        """
        query = select([cls.provincia]).where(cls.provincia.c.prov_direccion == prov_direccion)
        return query

    @classmethod
    def municipality_by_province(cls, *, prov_provincia):
        """
        Cuáles son las provincia con el prov_nombre igual
        """
        j = join(cls.provincia,municipio.Municipio.muni,cls.provincia.c.prov_id == municipio.Municipio.muni.c.prov_id)
        query = select([cls.provincia.c.prov_nombre,municipio.Municipio.muni.c.mun_nombre]).select_from(j).where(cls.provincia.c.prov_nombre == prov_provincia)
        
        return query