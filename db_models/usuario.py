from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select, join, and_
from config_vars import BBDD_CONNECTION

from municipio import Municipio
from nivel import Nivel
from nivel_beneficio import NivelBeneficio
from beneficio import Beneficio


Base = declarative_base()

class Usuario(Base):
    __tablename__ =  "usuario"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    #connection = engine.connect()
    metadata = MetaData()
    usuario = Table("usuario", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")

    @classmethod
    def all_users(cls):
        """
            Cuáles son los usuarios en la db
        """
        query = select([cls.usuario])
        return query

    @classmethod
    def single_user_by_id(cls, use_id):
        """
            Cual es el usuario por use_id
        """
        query = select([cls.usuario]).where(cls.usuario.c.use_id == use_id)
        return query
    
    @classmethod
    def user_by_dni(cls, use_dni):
        """
            Cual es el usuario por use_dni
        """
        query = select([cls.usuario]).where(cls.usuario.c.use_dni == use_dni)
        return query
    
    @classmethod
    def user_by_name(cls, use_nombre):
        """
            Cual es el usuario por use_nombre
        """
        query = select([cls.usuario]).where(cls.usuario.c.use_nombre == use_nombre)
        return query
    
    @classmethod
    def user_by_lastname(cls, use_apellido):
        """
            Cual es el usuario por use_apellido
        """
        query = select([cls.usuario]).where(cls.usuario.c.use_apellido == use_apellido)
        return query
    
    @classmethod
    def user_by_mail(cls, use_correo):
        """
            Cual es el usuario por use_correo
        """
        query = select([cls.usuario]).where(cls.usuario.c.use_correo == use_correo)
        return query
      

    @classmethod
    def user_by_municipality(cls, mun_id):
        """
            Cual es el usuario por use_id
        """
        j = join(
                cls.usuario,
                Municipio.muni,
                cls.usuario.c.mun_id ==  Municipio.muni.c.mun_id,
            )
        query =(
                 select([cls.usuario, Municipio.muni.c.mun_nombre])\
                .select_from(j)
                .where(cls.usuario.c.mun_id == mun_id)
            )
        return query
    

    @classmethod
    def user_level(cls, use_id, use_nombre):

        #Cuál es el nivel del usuario

        j = join(
            cls.usuario,
            NivelBeneficio.nivelBeneficio,
            cls.usuario.c.niv_ben_id == NivelBeneficio.nivelBeneficio.c.niv_ben_id
        ).join(
            Nivel.nivels,
            Nivel.nivels.c.niv_id == NivelBeneficio.nivelBeneficio.c.niv_id
        )

        query = (
            select([cls.usuario.c.use_dni, cls.usuario.c.use_nombre, Nivel.nivels.c.niv_nombre, Beneficio.bene.c.ben_nombre, Beneficio.bene.c.ben_descripcion])
            .select_from(j)
            .join(Beneficio.bene, Beneficio.bene.c.ben_id == NivelBeneficio.nivelBeneficio.c.ben_id)
            .where(
                and_(
                    cls.usuario.c.use_id == use_id,
                    cls.usuario.c.use_nombre == use_nombre
                )
            )
        )
        return query
   