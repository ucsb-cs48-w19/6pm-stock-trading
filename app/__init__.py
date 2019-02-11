#Creating application object as an instance of class 'Flask'

from flask import Flask
from config import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
Migrate = Migrate(app,db)

from app import models
