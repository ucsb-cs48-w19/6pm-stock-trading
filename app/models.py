from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(127), index=True, unique=True)
    email = db.Column(db.String(127), index=True, unique=True)
    password_hash = db.Column(db.String(127))
    
    def __repr__(self):
        return '<User {}{}{}>'.format(self.id, self.username,self.email)

class Profile(db.Model):
    birthday = db.Column(db.String(127))
    account = db.Column(db.Integer)
    investment = db.Column(db.Integer)

    def __repr__(self):
        return '<Profile {}{}{}>'.format(self.birthday, self.account, self.investment)

class Stock(db.Model):
    StockName = db.Column(db.String(127))
    price = db.Column(db.String(127))
    other_info1 = db.Column(db.String(127))
    other_info2 = db.Column(db.String(127))
    
    def __repr__(self):
        return '<Stock {}{}{}>'.format(self.StockName, self.price, self.other_info1)