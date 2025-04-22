from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app.config.auth import login_manager
from app.config.db import db, User

def create_app(config):

    app = Flask(__name__, template_folder = 'views')
    app.config.from_object(config)
    
    login_manager.init_app(app)
    db.init_app(app)

    @login_manager.user_loader
    def load_user(user_id: str) -> User:
        user = User.query.get(str(user_id))
        return user
    
    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/login', methods = ['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            user = User.query.filter_by(username = username, password = password).first()
            if user:
                login_user(username)
                return redirect(url_for('dashboard.html'))
            
    @app.route('/dashboard', methods = ['GET', 'POST'])
    def dashboard():
        if request.method == 'GET':
            return render_template('dashboard.html')
        
        if request.method == 'POST':
            redirect(url_for('logout'))
    

    @app.route('/logout', methods = ['GET', 'POST'])
    def logout():
        logout_user()
        redirect(url_for('login.html'))
    
    with app.app_context():
         # Creación de bases de datos
        db.create_all()

        # Instanciar usuarios
        user1 = User(username = 'camilo123', password = 'Camilo123')
        user2 = User(username = 'fulanitodetal', password = 'Fulano123')

    return app