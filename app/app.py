MYSQL_HOST = "3306"
MYSQL_USER = "root"
MYSQL_PASSWORD = "220961ez"
MYSQL_DB = "agencia_viajes"

from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

@app.route("/imagenes", methods=["POST"])
def crear_imagen():
    # Recibir datos de la imagen y almacenarlos en la base de datos
    ...

@app.route("/imagenes/<int:imagen_id>", methods=["PUT"])
def modificar_imagen(imagen_id):
    # Recibir datos actualizados y modificar la imagen en la base de datos
    ...

@app.route("/imagenes", methods=["GET"])
def obtener_imagenes():
    # Obtener todas las imágenes de la base de datos y devolverlas en formato JSON
    ...

@app.route("/imagenes/<int:imagen_id>", methods=["DELETE"])
def eliminar_imagen(imagen_id):
    # Eliminar la imagen con el ID especificado de la base de datos
    ...

if __name__ == "__main__":
    app.run(debug=True)