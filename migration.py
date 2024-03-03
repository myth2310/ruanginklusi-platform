from flask import Flask
from flask_mysqldb import MySQL
import hashlib

app = Flask(__name__)

# Konfigurasi MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ruangcerdas'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

with app.app_context():
    cur = mysql.connection.cursor()
    password = 'ruanginklusi'
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cur.execute('''
            INSERT INTO users (username, email, institusi, level, password) VALUES
            ('Admin-ruanginklusi', 'achmadmiftahudin2310@gmail.com', 'RuangInklusi', 'Admin', %s)
        ''', (hashed_password,))

    mysql.connection.commit()
    cur.close()


