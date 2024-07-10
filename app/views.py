from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Contacto  # Importa el modelo de Contact

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'  # URI de MySQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)  # Permitir solicitudes CORS

# Ruta para obtener todos los contactos
@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    contacts = Contacto.query.all()
    contact_list = []
    for contact in contacts:
        contact_list.append({
            'id': contact.id,
            'nombre': contact.nombre,
            'email': contact.email,
            'telefono': contact.telefono,
            'mensaje': contact.mensaje
        })
    return jsonify(contact_list), 200

# Ruta para agregar un nuevo contacto
@app.route('/api/contacts', methods=['POST'])
def add_contact():
    data = request.json
    new_contact = Contacto(nombre=data['nombre'], email=data['email'], telefono=data.get('telefono'), mensaje=data.get('mensaje'))
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({'message': 'Contacto agregado correctamente', 'id': new_contact.id}), 201

# Ruta para obtener un contacto por su ID
@app.route('/api/contacts/<int:id>', methods=['GET'])
def get_contact(id):
    contact = Contacto.query.get_or_404(id)
    return jsonify({
        'id': contact.id,
        'nombre': contact.nombre,
        'email': contact.email,
        'telefono': contact.telefono,
        'mensaje': contact.mensaje
    }), 200

# Ruta para actualizar un contacto existente por su ID
@app.route('/api/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    contact = Contacto.query.get_or_404(id)
    data = request.json
    contact.nombre = data['nombre']
    contact.email = data['email']
    contact.telefono = data.get('telefono')
    contact.mensaje = data.get('mensaje')
    db.session.commit()
    return jsonify({'message': 'Contacto actualizado correctamente'}), 200

# Ruta para eliminar un contacto por su ID
@app.route('/api/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contacto.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify({'message': 'Contacto eliminado correctamente'}), 200

if __name__ == '__main__':
    app.run(debug=True)
