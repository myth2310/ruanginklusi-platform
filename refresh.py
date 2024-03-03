from flask import Flask
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ruangcerdas'
mysql = MySQL(app)

app.config['UPLOAD_FILE_ARTIKEL'] = 'static/images/artikel/'

with app.app_context():
    cur = mysql.connection.cursor()

    #Detection Average
    cur.execute("DELETE FROM users")
    cur.execute("ALTER TABLE users DROP user_id")
    cur.execute("ALTER TABLE users ADD  user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")

    cur.execute("DELETE FROM speech")
    cur.execute("ALTER TABLE speech DROP speech_id")
    cur.execute("ALTER TABLE speech ADD  speech_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")

    cur.execute("DELETE FROM sign")
    cur.execute("ALTER TABLE sign DROP sign_id")
    cur.execute("ALTER TABLE sign ADD  sign_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")

    cur.execute("DELETE FROM article")
    cur.execute("ALTER TABLE article DROP article_id")
    cur.execute("ALTER TABLE article ADD  article_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")


    def delete_artikel_files():
        upload_dir = app.config['UPLOAD_FILE_ARTIKEL']
        for filename in os.listdir(upload_dir):
            file_path = os.path.join(upload_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

delete_artikel_files()