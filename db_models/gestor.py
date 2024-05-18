
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select
from config_vars import BBDD_CONNECTION


Base = declarative_base()

class Gestor(Base):
    __tablename__ =  "gestor"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    connection = engine.connect()
    metadata = MetaData()
    gestor = Table("gestor", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")

    @classmethod
    def all_managers(cls):
        """
            Cuáles son los gestores en la db
        """
        query = select([cls.gestor])
        return query

    @classmethod
    def single_manager(cls, *, ges_id):
        """
            Cual es el gestor por ges_id
        """
        query = select([cls.gestor]).where(cls.gestor.c.ges_id == ges_id)
        return query

    @classmethod
    def single_manager_by_DNI(cls, *, ges_DNI):
        """
            Cual es el gestor por DNI
        """
        query = select([cls.gestor]).where(cls.gestor.c.ges_dni == ges_DNI)
        return query

    @classmethod
    def single_manager_by_name(cls, *, ges_nombre):
        """
            Cual es el gestor por nombre
        """
        query = select([cls.gestor]).where(cls.gestor.c.ges_nombre == ges_nombre)
        return query
    
    @classmethod
    def single_manager_by_lastname(cls, *, ges_apellido):
        """
            Cual es el gestor por apellido
        """
        query = select([cls.gestor]).where(cls.gestor.c.ges_apellido == ges_apellido)
        return query