from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select, join
from config_vars import BBDD_CONNECTION


Base = declarative_base()

class Nivel(Base):
    __tablename__ =  "nivel"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    metadata = MetaData()
    nivels = Table("nivel", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    
    @classmethod
    def parameters_by_id(cls,niv_id):
        """
        Cuáles son los parámetros
        """
        query = select([cls.nivels]).where(cls.nivels.c.niv_id == niv_id)
        return query
    
    @classmethod
    def all_levels(cls):
        """
        Cuáles son los niveles (en caso de no pasar parámetros)
        """
        query = select([cls.nivels])
        return query

    @classmethod
    def single_level(cls, niv_id):
        """
        Cuáles son los niveles con el niv_id
        """
        query = select([cls.nivels]).where(cls.nivels.c.niv_id == niv_id)
        return query
    
    @classmethod
    def single_level_by_name(cls, niv_nombre):
        """
        Cuáles son los niveles con el niv_nombre igual
        """
        query = select([cls.nivels]).where(cls.nivels.c.niv_nombre.like(f'%{niv_nombre}%'))
        return query
 