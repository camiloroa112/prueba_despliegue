from flask_alchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    username = db.Column(db.String(50), nullable = False)

class Heladeria(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
class Producto(db.Model):
    pass

class Ingredientes(db.Model):
    pass