from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(127), index=True, unique=True)
    email = db.Column(db.String(127), index=True, unique=True)
    password_hash = db.Column(db.String(127))
    other_info1 = db.Column(db.String(127))
    other_info2 = db.Column(db.String(127))
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Stock(db.Model):
    StockName = db.Column(db.String(127))
    price = db.Column(db.String(127))
    other_info1 = db.Column(db.String(127))
    other_info2 = db.Column(db.String(127))