from flask import Flask, render_template, Response,request, redirect, url_for,session,flash,jsonify
from flask_mysqldb import MySQL
import hashlib
from datetime import datetime
import os
from werkzeug.utils import secure_filename
import cv2
import numpy as np
# import pyttsx3
# from detection import frames
import time
import sys
from data import data 
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import base64

load_dotenv()


app = Flask(__name__)
cap = cv2.VideoCapture(0)
app.secret_key = 'ruangcerdas'

# Konfigurasi MySQL
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_CURSORCLASS'] = os.getenv('MYSQL_CURSORCLASS')
mysql = MySQL(app)

app.config['UPLOAD_FOLDER'] = 'static/images/artikel'
app.config['UPLOAD_PROFIL'] = 'static/images/profil'

key = base64.urlsafe_b64encode(os.urandom(32))
cipher_suite = Fernet(key)

def encrypt_id(id):
    id_str = str(id).encode('utf-8')
    encrypted_id = cipher_suite.encrypt(id_str)
    return encrypted_id.decode('utf-8')

def decrypt_id(encrypted_id):
    encrypted_id = encrypted_id.encode('utf-8')
    decrypted_id = cipher_suite.decrypt(encrypted_id)
    return int(decrypted_id.decode('utf-8'))

@app.context_processor
def utility_processor():
    return dict(encrypt_id=encrypt_id)

    
#Landing Page
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM article ORDER BY RAND() LIMIT 3")
    data = cur.fetchall()
    return render_template('landing-page/index.html',data=data)


@app.route('/about')
def about():
    return render_template('landing-page/about.html')

@app.route('/<string:slug>')
def articles(slug):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM article WHERE slug = %s",(slug,))
    artikel = cur.fetchone()
    return render_template('landing-page/articles.html',artikel=artikel)

#Dashboard
@app.route('/dashboard')
def dashboard():
    if 'islogin' in session:
        page = 'Dashboard'
        cur = mysql.connection.cursor()

        cur.execute("SELECT COUNT(*) FROM users WHERE level='Pengguna'")
        result_users = cur.fetchone()
        count_users = result_users['COUNT(*)']

        cur.execute("SELECT COUNT(*) FROM users WHERE level='Admin'")
        result_admin = cur.fetchone()
        count_admin = result_admin['COUNT(*)']

        cur.execute("SELECT COUNT(*) FROM article")
        result_artikel = cur.fetchone()
        count_artikel = result_artikel['COUNT(*)']

        cur.execute("SELECT * FROM article ORDER BY RAND() LIMIT 3")
        data = cur.fetchall()
        
        return render_template('dashboard/index.html',page=page,data=data,count_users=count_users,count_admin=count_admin,count_artikel=count_artikel)
    else:
        return redirect(url_for('signIn'))
  
@app.route('/users')
def users():
    if 'islogin' in session:
        page = 'Users'
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users")
        data = cur.fetchall()
        users_with_time_diff = []
        for user in data:
            modified_user = user.copy() 

            if isinstance(user['last_login'], str):
                last_login_time = datetime.strptime(user['last_login'], '%Y-%m-%d %H:%M:%S')
            elif isinstance(user['last_login'], datetime):
                last_login_time = user['last_login']
            else:
                last_login_time = None

            if last_login_time:
                time_difference = datetime.now() - last_login_time
                if time_difference.days > 0:
                    modified_user['last_login_diff'] = f'{time_difference.days} days ago'
                else:
                    hours, remainder = divmod(time_difference.seconds, 3600)
                    minutes, _ = divmod(remainder, 60)
                    modified_user['last_login_diff'] = f'{hours} hours, {minutes} minutes ago'
            else:
                modified_user['last_login_diff'] = 'Never logged in'

            users_with_time_diff.append(modified_user)

        return render_template('dashboard/users-page.html', page=page, data=users_with_time_diff)
    else:
        return redirect(url_for('signIn'))

@app.route('/artikel')
def artikel():
    if 'islogin' in session:
        page = 'Artikel'
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM article")
        data = cur.fetchall()
        return render_template('dashboard/artikel-page.html',page=page,data=data)
    else:
        return redirect(url_for('signIn'))

@app.route('/form-add-artikel')
def formAddArtikel():
    if 'islogin' in session:
        page = 'Form Tambah Artikel'
        return render_template('dashboard/form-add-artikel.html',page=page)
    else:
        return redirect(url_for('signIn'))


@app.route('/edit-artikel/<int:article_id>', methods=['GET', 'POST'])
def formEditArtikel(article_id):
    if 'islogin' in session:
        if request.method == 'GET':
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM article WHERE article_id = %s", (article_id,))
            data = cur.fetchone()
            cur.close()
            if data:
                page = 'Form Edit Artikel'
                return render_template('dashboard/form-edit-artikel.html', page=page, data=data)
            else:
                flash('Artikel tidak ditemukan.', 'error')
                return redirect(url_for('artikel'))
        elif request.method == 'POST':
            title = request.form.get('title')
            kategori = request.form.get('kategori')
            description = request.form.get('description')

            if not title or not kategori or not description:
                flash('Harap isi semua kolom.', 'error')
                return redirect(url_for('artikel'))

            date = datetime.now()
            slug = title.lower().replace(' ', '-')
            summary = ' '.join(description.split()[:20])

            if 'image' not in request.files:
                flash('Tidak ada file gambar yang diunggah.', 'error')
                return redirect(url_for('artikel'))

            image = request.files['image']
            if image.filename == '':
                flash('Tidak ada file gambar yang diunggah.', 'error')
                return redirect(url_for('artikel'))

            file_extension = os.path.splitext(image.filename)[1]
            filename = secure_filename(title) + file_extension

            upload_dir = os.path.join(app.config['UPLOAD_FOLDER'])
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)
            file_path = os.path.join(upload_dir, filename)
            image.save(file_path)

            cur = mysql.connection.cursor()
            cur.execute("""
                UPDATE article
                SET title = %s, kategori = %s, date = %s, slug = %s, description = %s, summary = %s, image = %s
                WHERE article_id = %s
            """, (title, kategori, date, slug, description, summary, filename, article_id))

            mysql.connection.commit()
            cur.close()

            flash('Artikel berhasil diupdate.', 'success')
            return redirect(url_for('artikel'))
    else:
        return redirect(url_for('signIn'))


@app.route('/profil')
def profil():
    if 'islogin' in session:
        page = 'Profil'
        user_id = session['user_id']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users where user_id =%s",(user_id,))
        data = cur.fetchone()
        return render_template('dashboard/profil-page.html',page=page,data=data)
    else:
        return redirect(url_for('signIn'))

@app.route('/detail-speech')
def detailSpeech():
    if 'islogin' in session:
        page = 'Detail Speech'
        user_id = session['user_id']
        with mysql.connection.cursor() as cur:
            cur.execute("SELECT speech.*, users.* FROM speech INNER JOIN users ON speech.user_id = users.user_id WHERE speech.user_id = %s", (user_id,))
            data = cur.fetchone()
        return render_template('dashboard/speech-page.html', page=page, data=data)
    else:
        return redirect(url_for('signIn'))
     
@app.route('/edit-speech/<int:speech_id>', methods=['GET', 'POST'])
def edit_speech(speech_id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        type_camera = request.form['type_camera']
        ip_camera = request.form['ip_camera'] or '0'
        bahasa = request.form['bahasa']
        cur.execute("UPDATE speech SET type_camera=%s, ip_camera=%s, bahasa=%s WHERE speech_id=%s",
                    (type_camera, ip_camera, bahasa, speech_id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('detailSpeech'))
  
@app.route('/speech-live/<encrypted_speech_id>')
def speechLive(encrypted_speech_id):
    if 'islogin' in session:
        try:
            speech_id = decrypt_id(encrypted_speech_id)
        except Exception as e:
            return "Invalid ID", 400

        page = 'Speech to Text Live'
        with mysql.connection.cursor() as cur:
            cur.execute("SELECT * FROM speech WHERE speech_id = %s", (speech_id,))
            data = cur.fetchone()
        
        return render_template('dashboard/live-speech.html', page=page, data=data)
    else:
        return redirect(url_for('signIn'))


background_blur_strength = 15
def generate_frames(cap):
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)
            blurred_background = cv2.GaussianBlur(frame, (background_blur_strength, background_blur_strength), 0)
            result = cv2.bitwise_and(frame, frame, mask=mask_inv)
            result += cv2.bitwise_and(blurred_background, blurred_background, mask=mask)
            ret, buffer = cv2.imencode('.jpg', result)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    ip_camera_address = session.get('ip_camera', '0')
    if ip_camera_address != '0':
        cap = cv2.VideoCapture(f'http://{ip_camera_address}:8080/video')
    else:
        cap = cv2.VideoCapture(0)
    return Response(generate_frames(cap), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/detail-sign-detection')
def detailSign():
    if 'islogin' in session:
        page = 'Detail Sign Detection'
        user_id = session['user_id']
        with mysql.connection.cursor() as cur:
            cur.execute("SELECT sign.*, users.* FROM sign INNER JOIN users ON sign.user_id = users.user_id WHERE sign.user_id = %s", (user_id,))
            data = cur.fetchone()
        return render_template('dashboard/sign-detection.html',page=page,data=data)

@app.route('/detail-sign-language')
def detailSignLanguage():
    if 'islogin' in session:
        page = 'Detail Sign Lenguage'
        return render_template('dashboard/sign-language-page.html',page=page)
    else:
        return redirect(url_for('signIn'))
    
@app.route('/edit-sign/<int:sign_id>', methods=['GET', 'POST'])
def edit_sign(sign_id):
    cur = mysql.connection.cursor()
    type_camera = request.form['type_camera']
    voice = request.form['voice']
    ip_camera = request.form['ip_camera'] or '0'
    cur.execute("UPDATE sign SET type_camera=%s, voice=%s, ip_camera=%s WHERE sign_id=%s",
                (type_camera, voice,ip_camera,sign_id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('detailSign'))

#Auth
@app.route('/sign-up')
def signUp():
    return render_template('sign-up.html')

#Action
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        institusi = request.form['institusi']
        password = request.form['password']
        level = 'Pengguna'
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cur.fetchone()
        cur.close()

        if existing_user:
            flash("Email sudah terdaftar. Gunakan email lain.", 'error')
            return redirect(url_for('signUp'))

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, email, institusi, level, password) VALUES (%s, %s, %s, %s, %s)",
                    (username, email, institusi, level, hashed_password))
        
        user_id = cur.lastrowid
        bahasa = 'id'
        cur.execute("INSERT INTO speech (user_id, type_camera, ip_camera, bahasa) VALUES (%s, 'Internal', '0', %s)",
                    (user_id, bahasa))
        
        cur.execute("INSERT INTO sign (user_id, type_camera,voice,ip_camera) VALUES (%s, 'Internal',0,'0')",
                    (user_id,))
        
        mysql.connection.commit()
        cur.close()

        flash("Pendaftaran berhasil.", 'success')
        return redirect(url_for('index'))

    return render_template('register.html') 

@app.route('/insert-artikel', methods=['GET', 'POST'])
def insertArtikel():
    title = request.form['title']
    kategori = request.form['kategori']
    date = datetime.now()
    slug = title.lower().replace(' ', '-')
    description = request.form['description']
    summary = ' '.join(description.split()[:20])

    image = request.files['image']
    if image.filename != '':
        # Mengambil ekstensi file dari nama asli gambar
        file_extension = os.path.splitext(image.filename)[1]
        
        # Membuat nama file baru dari judul artikel
        filename = secure_filename(title) + file_extension

        upload_dir = os.path.join(app.config['UPLOAD_FOLDER'])
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        file_path = os.path.join(upload_dir, filename)
        image.save(file_path)

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO article (title, kategori, date, slug, description, summary, image) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (title, kategori, date, slug, description, summary, filename))

    mysql.connection.commit()
    cur.close()
    flash("Artikel berhasil ditambahkan.", 'success')
    return redirect(url_for('artikel'))

#Auth/Login
@app.route('/sign-in', methods=['GET', 'POST'])
def signIn():
    if 'islogin' in session:
        return redirect(url_for('dashboard'))
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password'] 
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        account = cursor.fetchone()
        if account and check_password(password, account['password']):
            session['islogin'] = True
            session['user_id'] = account['user_id']
            session['level'] = account['level']
            session['username'] = account['username']

             # Update last_login and online_status in the database
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('''
                UPDATE users
                SET last_login = %s, online_status = TRUE
                WHERE user_id = %s
            ''', (now, account['user_id']))

            mysql.connection.commit()
            return redirect(url_for('dashboard'))
        else:
            flash("User Tidak Ditemukan atau Password Salah",'error')
            return redirect(url_for('signIn'))
    else:
        return render_template('sign-in.html')
  
def check_password(input_password, stored_password):
    hashed_input_password = hashlib.sha256(input_password.encode()).hexdigest()
    return hashed_input_password == stored_password

@app.route('/accept-speech/<int:speech_id>', methods=['POST'])
def acceptSpeech(speech_id):
    if 'islogin' in session:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE speech SET accept = 1 WHERE speech_id = %s", (speech_id,))
        mysql.connection.commit()
        cur.execute("SELECT * FROM speech WHERE speech_id = %s", (speech_id,))
        data = cur.fetchone()
        return redirect(url_for('speechLive', speech_id=data['speech_id']))
    else:
        return redirect(url_for('signIn'))
    
@app.route('/accept-sign/<int:sign_id>', methods=['POST'])
def acceptSign(sign_id):
    if 'islogin' in session:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE sign SET accept = 1 WHERE sign_id = %s", (sign_id,))
        mysql.connection.commit()
        cur.execute("SELECT * FROM sign WHERE sign_id = %s", (sign_id,))
        data = cur.fetchone()
        return redirect(url_for('signLive', sign_id=data['sign_id']))
    else:
        return redirect(url_for('signIn'))
    
@app.route('/delete_selected', methods=['POST'])
def delete_selected():
    selected_article = request.form.getlist('selected_article')
    if selected_article:
        cursor = mysql.connection.cursor()
        query = "DELETE FROM article WHERE article_id IN ({})".format(','.join(['%s'] * len(selected_article)))
        cursor.execute(query, tuple(selected_article))
        mysql.connection.commit()
        cursor.close()
    return redirect(url_for('artikel'))

@app.route('/logout')
def logout():
    if 'islogin' in session:
        user_id = session.get('user_id')
        cur = mysql.connection.cursor()
        cur.execute('UPDATE users SET online_status = FALSE WHERE user_id = %s', (user_id,))
        mysql.connection.commit()
        cur.close()
        session.pop('islogin',None)
        session.clear()
    return redirect(url_for('signIn'))

@app.route('/data')
def data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT level, COUNT(*) as total FROM users GROUP BY level")
    data = cur.fetchall()
    labels = []
    values = []
    for row in data:
        labels.append(row['level'])
        values.append(row['total'])
    print(labels)
    print(values)
    return jsonify({'labels': labels, 'values': values})

@app.route('/sign-detection-live/<int:sign_id>')
def signLive(sign_id):
    if 'islogin' in session:
        global voice_id
        page = 'Sign Detection Live'
        with mysql.connection.cursor() as cur:
            cur.execute("SELECT * FROM sign WHERE sign_id = %s", (sign_id,))
            data = cur.fetchone()
            session['ip_camera'] = data['ip_camera']
            voice_id = data['voice']
        return render_template('dashboard/live-sign-detection.html',page=page,data=data,voice_id=voice_id)
    else:
        return redirect(url_for('signIn'))
        
# @app.route('/video')
# def video():
#     ip_camera_address = session.get('ip_camera', '0')
#     if ip_camera_address != '0':
#         cap = cv2.VideoCapture(f'http://{ip_camera_address}:8080/video')
#     else:
#         cap = cv2.VideoCapture(0)
#     return Response(frames(cap), mimetype='multipart/x-mixed-replace; boundary=frame')

import time
import sys
from data import data 

def get_video_list(kata):
    videoList = []
    print(kata)
    for category, videos in data.items():
        for video_name in videos:
            index = (" %s " % kata.lower()).find(" %s " % video_name)
            if index >= 0:
                videoList.append({'category': category, 'video_name': video_name})
    print(videoList)
    return videoList, set(category for category, _ in videoList)

@app.route('/process_speech', methods=['POST'])
def process_speech():
    data = request.json
    kata = data.get('kata', '')
    
    if not kata:
        result = "Maaf, tidak dapat mengenali suara"
        videoList = []
        categories = set()
    else:
        videoList, categories = get_video_list(kata)
        result = f"Kata yang dikenali: {kata}"
        
    return jsonify({'result': result, 'videoList': videoList, 'categories': list(categories)})

@app.route('/speech-sign-language')
def liveSpeechSignLanguage():
    if 'islogin' in session:
        page = 'Speech to Sign Language Live'
        return render_template('dashboard/live-sign-language.html',page=page,  result="", videoList=[], categories=set())
    else:
        return redirect(url_for('signIn'))


def get_vidio(input_text):
    videoList = []
    for category, videos in data.items():
        for video_name in videos:
            index = (" %s " % input_text.lower()).find(" %s " % video_name)
            if index >= 0:
                videoList.append({'category': category, 'video_name': video_name})
        
        print("Video list:", videoList)
  
    return videoList, set(category for category, _ in videoList)

@app.route('/process_input', methods=['POST'])
def process_input():
    data = request.json
    input_text = data.get('input_text', '')

    if not input_text:
        input_text = request.form.get('textInput', '')

    if not input_text:
        result = "Maaf, tidak dapat mengenali input"
        videoList = []
        categories = set()
    else:
        videoList, categories = get_vidio(input_text)
        result = f"Transcribe : {input_text}"

    return jsonify({'result': result, 'videoList': videoList, 'categories': list(categories)})

@app.route('/text-sign-language')
def liveTextSignLanguage():
    if 'islogin' in session:
        page = 'Text to Sign Language Live'
        return render_template('dashboard/text-to-language.html',page=page)
    else:
        return redirect(url_for('signIn'))
    
@app.route('/coba')
def coba():
    return render_template('coba.html')

    
@app.route('/edit-profil/<int:user_id>', methods=['GET', 'POST'])
def edit_profil(user_id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        username = request.form['username']
        institusi = request.form['institusi']
        no_hp = request.form['no_hp']
        alamat = request.form['alamat']

        image = request.files['image']
        if image.filename != '':
            file_extension = os.path.splitext(image.filename)[1]
            filename = secure_filename(username) + file_extension

            upload_dir = os.path.join(app.config['UPLOAD_PROFIL'])
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)
            file_path = os.path.join(upload_dir, filename)
            image.save(file_path)

        cur.execute("UPDATE users SET image=%s, username=%s, institusi=%s, no_hp=%s, alamat=%s WHERE user_id=%s",
                    (filename, username, institusi, no_hp,alamat,user_id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('profil'))
    
if __name__ == '__main__':
    app.run(debug=True, threaded=True)



