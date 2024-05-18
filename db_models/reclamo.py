from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select, join
from config_vars import BBDD_CONNECTION
from datetime import date  

from municipio import Municipio
from estado import Estado
from categoria import Categoria
from criticidad import Criticidad
from usuario import Usuario

Base = declarative_base()

class Reclamo(Base):
    __tablename__ =  "reclamo"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    metadata = MetaData()
    rec = Table("reclamo", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    
    @classmethod
    def parameters_by_id(cls, *,rec_id ):
        """
        Cuáles son los parámetros
        """
        query = select([cls.rec]).where(cls.rec.c.rec_id == rec_id)
        return query

    @classmethod
    def all_claims(cls):
        """
        Cuáles son los beneficios
        """
        query = select([cls.rec])
        return query
    
    @classmethod
    def single_claim(cls, rec_id):
        """
        Cuáles son los reclamos por rec_id
        """

        query = select([cls.rec]).where(cls.rec.c.rec_id == rec_id)
        return query
    @classmethod
    def claims_by_tittle(cls, rec_titulo):
        """
        Cuáles son los reclamos por rec_id
        """

        query = select([cls.rec]).where(cls.rec.c.rec_titulo.like(f'%{rec_titulo}%'))
        return query
    
    
    @classmethod
    def claims_by_municipality(cls, mun_id):
        """
        Cuáles son los reclamos por municipio
        """
        j = join(
                cls.rec,
                Municipio.muni,
                cls.rec.c.mun_id ==  Municipio.muni.c.mun_id,
            )
        query = (
                select([cls.rec.c.rec_titulo, cls.rec.c.rec_descripcion, Municipio.muni.c.mun_nombre ])
                .select_from(j)
                .where(cls.rec.c.mun_id == mun_id)
            )
       
        return query
    
    @classmethod
    def claims_by_status(cls, est_id):
        """
        Cuáles son los reclamos por estado
        """
        j = join(
                cls.rec,
                Estado.estado,
                cls.rec.c.est_id ==  Estado.estado.c.est_id,
            )
        query = (
                select([cls.rec.c.rec_titulo, cls.rec.c.rec_descripcion, Estado.estado.c.est_nombre.label('estado_nombre')])
                .select_from(j)
                .where(cls.rec.c.est_id == est_id)
            )
        return query
    
    @classmethod
    def claims_by_user(cls, use_id):
        """
        Cuáles son los reclamos por usuario
        """
        j = join(
                cls.rec,
                Usuario.usuario,
                cls.rec.c.use_id ==  Usuario.usuario.c.use_id,
            )
        query = (
                select([cls.rec.c.rec_titulo, cls.rec.c.rec_descripcion, Usuario.usuario.c.use_nombre,Usuario.usuario.c.use_apellido, Usuario.usuario.c.use_dni])
                .select_from(j)
                .where(cls.rec.c.use_id == use_id)
            )
        return query
    @classmethod
    def claims_by_category(cls, cat_id):
        """
        Cuáles son los reclamos por categoria
        """
        j = join(
                cls.rec,
                Categoria.cate,
                cls.rec.c.cat_id ==  Categoria.cate.c.cat_id,
            )
        query = (
                select([cls.rec.c.rec_titulo, cls.rec.c.rec_descripcion, Categoria.cate.c.cat_nombre ])
                .select_from(j)
                .where(cls.rec.c.cat_id == cat_id)
            )
        return query
    
    @classmethod
    def claims_by_criticity(cls, cri_id):
        """
        Cuáles son los reclamos por criticidad
        """
        j = join(
                cls.rec,
                Criticidad.criticidad,
                cls.rec.c.cri_id ==  Criticidad.criticidad.c.cri_id,
            )
        query = (
                select([cls.rec.c.rec_titulo, cls.rec.c.rec_descripcion, Criticidad.criticidad.c.cri_nombre ])
                .select_from(j)
                .where(cls.rec.c.cri_id == cri_id)
            )
        return query