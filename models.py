#from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from flask_login import UserMixin
#Imports for postgres hosting
from app import db, login

#db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(100))
    initial_investment = db.Column(db.Float)
    balance = db.Column(db.Float)
    risk = db.Column(db.Boolean)

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.set_password(password)
        self.initial_investment = 0
        self.balance = 0
        self.risk = False

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)
    
    def check_hash(self, passwordHashed):
        return self.pwdhash == passwordHashed

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def set_risk(risk):
        self.risk = risk
