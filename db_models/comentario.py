
import sys
import os
dirname = os.path.dirname(__file__)
 
sys.path.append(dirname)
sys.path.append(dirname+"/db_models/")

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select,join
from config_vars import BBDD_CONNECTION
from datetime import date  

from reclamo import Reclamo
from gestor import Gestor
from usuario import Usuario

Base = declarative_base()

class Comentario(Base):
    __tablename__ =  "comentario"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    metadata = MetaData()
    comen = Table("comentario", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    
    @classmethod
    def parameters_by_id(cls, *,com_id ):
        """
        Cuáles son los parámetros
        """
        query = select([cls.comen]).where(cls.comen.c.com_id == com_id)
        return cls.connection.execute(query).fetchall()

    @classmethod
    def all_coments(cls):
        """
        Cuáles son los beneficios
        """
        query = select([cls.comen])
        return query
        
    @classmethod
    def single_comment(cls, com_id):
        """
        Cuáles son los comentario por com_id
        """
        query = select([cls.comen]).where(cls.comen.c.com_id == com_id)
        return query
        
    @classmethod
    def older_comment(cls):
        """
        Cuál es el comentario más antiguo
        """
        query = select([cls.comen]).where(cls.comen.c.com_fecha_creacion <= date.today()).order_by(cls.comen.c.com_fecha_creacion).limit(1)
        return query
    
    @classmethod
    def comments_by_user(cls, use_id):
        """
        Cuáles son los comentario por com_id
        """
        query = select([cls.comen]).where(cls.comen.c.use_id == use_id)
        return query
    
    @classmethod
    def comments_by_manager(cls, ges_id):
        """
        Cuáles son los comentario por com_id
        """
        query = select([cls.comen]).where(cls.comen.c.ges_id == ges_id)
        return query

    @classmethod
    def comments_by_claims(cls, rec_id):
        """
        Cuáles son los comentario por com_id
        """
        j=j = join(
    cls.comen,
    Reclamo.rec,
    cls.comen.c.rec_id == Reclamo.rec.c.rec_id
).join(
    Usuario.usuario,
    Reclamo.rec.c.use_id == Usuario.usuario.c.use_id
).join(
    Gestor.gestor,
    cls.comen.c.ges_id == Gestor.gestor.c.ges_id
)
        
        query = select([Usuario.usuario.c.use_nombre, Gestor.gestor.c.ges_nombre,Reclamo.rec.c.rec_titulo , cls.comen.c.com_texto]).select_from(j).where(cls.comen.c.rec_id == rec_id)
        return query
