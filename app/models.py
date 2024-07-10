from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    comentario = db.Column(db.Text, nullable=False)
    tema = db.Column(db.String(255), nullable=False)
    medio_contacto = db.Column(db.String(255), nullable=False)
    archivo = db.Column(db.String(255))

    def __init__(self, nombre, email, comentario, tema, medio_contacto, archivo=None):
        self.nombre = nombre
        self.email = email
        self.comentario = comentario
        self.tema = tema
        self.medio_contacto = medio_contacto
        self.archivo = archivo

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'comentario': self.comentario,
            'tema': self.tema,
            'medio_contacto': self.medio_contacto,
            'archivo': self.archivo
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Contacto.query.all()

    @staticmethod
    def get_by_id(contacto_id):
        return Contacto.query.get(contacto_id)
