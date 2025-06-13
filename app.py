from flask import Flask, redirect, url_for, session, render_template, request
from authlib.integrations.flask_client import OAuth
import os
from uuid import uuid4
import mysql.connector

app = Flask(__name__)
app.secret_key = os.urandom(24)

# OAuth Google  /  Aqui que é a configuração do SSO (Single Sign-on), buscando o ID cliente, e o secret key configurada
#               /                                                                                     la no Google Cloud
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='Client ID',  #Client ID
    client_secret='Client Secret',  #Client Secret
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)

# Conexão com Banco de dados
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="****",
        database="database"
    )

# Rota de abertura da API
@app.route('/')
def index():
    user = session.get('user')
    if user:
        return render_template('home.html', user=user)
    return render_template('login.html')

# Rota para executar o login com a Google, e definir a URL de retorno
@app.route('/login')
def login():
    nonce = uuid4().hex 
    session['nonce'] = nonce 
    redirect_uri = url_for('auth_callback', _external=True) #dominio.com/auth/callback
    return google.authorize_redirect(redirect_uri, nonce=nonce) #URL de retorno

# Rota para receber o token
@app.route('/auth/callback')
def auth_callback():
    token = google.authorize_access_token()
    user_info = google.parse_id_token(token, nonce=session.get('nonce'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Verifica se usuário existe
    cursor.execute("SELECT * FROM users WHERE email = %s", (user_info['email'],))
    user = cursor.fetchone()

    # Se não existir, cria um e insere no banco de dados
    if not user:
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (user_info['name'], user_info['email']))
        conn.commit()

    cursor.close()
    conn.close()

    session['user'] = user_info
    return redirect('/')

# Rota para executar o login manualmente
@app.route('/usuario', methods=['GET', 'POST'])
def usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users WHERE name = %s AND email = %s AND senha = %s", (nome, email, senha))
        user = cursor.fetchone()

        if not user:
            cursor.execute("INSERT INTO users (name, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
            conn.commit()

            cursor.execute("SELECT * FROM users WHERE name = %s AND email = %s AND senha = %s", (nome, email, senha))
            user = cursor.fetchone()

        session['user'] = user

        print(user)
        return render_template('home.html', user=user)

    user = session.get('user')
    

    return redirect('home.html', user=user)
# Rota para executar o logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
