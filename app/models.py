from sqlalchemy import Column, Integer, String, Text

class Imagen(Base):
    __tablename__ = "imagenes"

    id_imagen = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=False)
    ruta = Column(String(255), nullable=False)
    fecha_creacion = Column(DATETIME, NOT NULL, DEFAULT CURRENT_TIMESTAMP)
    usuario_id = Column(Integer, not null)

class Usuario(BaseException):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    correo_electronico = Column(String(255), nullable=False, unique=True)
    contrasena = Column(String(255), nullable=False)