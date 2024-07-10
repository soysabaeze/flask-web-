import os
import mysql.connector
from flask import g
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos usando variables de entorno
DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'), 
    'password': os.getenv('DB_PASSWORD'), 
    'host': os.getenv('DB_HOST'), 
    'database': os.getenv('DB_NAME'), 
    'port': os.getenv('DB_PORT', 3306) 
}


