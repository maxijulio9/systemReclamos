import sys
import os
dirname = os.path.dirname(__file__)
 
sys.path.append(dirname)
sys.path.append(dirname+"/db_models/")

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select,join
from config_vars import BBDD_CONNECTION
from datetime import date  

from db_models import nivel
from db_models import nivel_beneficio

Base = declarative_base()

class Beneficio(Base):
    __tablename__ =  "beneficios"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    connection = engine.connect()
    metadata = MetaData()
    bene = Table("beneficios", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    
    @classmethod
    def parameters_by_id(cls, *,ben_id ):
        """
        Cuáles son los parámetros
        """
        query = select([cls.bene]).where(cls.bene.c.ben_id == ben_id)
        return cls.connection.execute(query).fetchall()

    @classmethod
    def all_benefits(cls):
        """
        Cuáles son los beneficios
        """

        query = select([cls.bene])
        return query
    
    @classmethod
    def single_benefit(cls,*, ben_id):
        """
        Cuáles son los beneficios por ben_id
        """

        query = select([cls.bene]).where(cls.bene.c.ben_id == ben_id)
        return query

    @classmethod
    def benefit_closest_to_expiration(cls):
        """
        Cuál es el beneficio más próximo a vencer
        """
        ''' 
        SELECT *
        FROM beneficios
        WHERE fecha_expiracion >= CURRENT_DATE
        ORDER BY fecha_expiracion
        LIMIT 1;

        '''
        query = select([cls.bene]).where(cls.bene.c.ben_fecha_de_expiracion >= date.today()).order_by(cls.bene.c.ben_fecha_de_expiracion).limit(1)
        return query

    @classmethod
    def benefit_by_name(cls,*,ben_nombre):
        query = select([cls.bene]).where(cls.bene.c.ben_nombre == ben_nombre)
        return query
        
    @classmethod
    def benefit_by_level(cls,*,niv_id):
        '''
        beneficio segun nivel id
        '''
        j = join(cls.bene,nivel_beneficio.NivelBeneficio.nivelBeneficio,cls.bene.c.ben_id==nivel_beneficio.NivelBeneficio.nivelBeneficio.c.ben_id)
        
        query = select([nivel_beneficio.NivelBeneficio.nivelBeneficio.c.ben_id,cls.bene.c.ben_nombre,cls.bene.c.ben_descripcion]).select_from(j).where(nivel_beneficio.NivelBeneficio.nivelBeneficio.c.niv_id==niv_id)
        
        return query