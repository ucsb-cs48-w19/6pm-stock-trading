#from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
#Imports for postgres hosting
from app import db

#db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(100))
    initial_investment = db.Column(db.Float)
    balance = db.Column(db.Float)

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.set_password(password)
        self.initial_investment = 0
        self.balance = 0

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)
    #for postgresql hosting
    def __repr__(self):
        return '<uid {}>'.format(self.uid)

    def set_initial_investment(initial_investment):
        self.initial_investment = initial_investment

