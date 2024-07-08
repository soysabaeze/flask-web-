from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL
app = Flask(__name__)
mysql = MySQL()

mysql.init_app (app)

if __name__ == '__main__':
   app.run(debug=True)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '220961ez'
app.config['MYSQL_DATABASE_DB'] = 'agencia_viajes'