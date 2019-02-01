from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(127), index=True, unique=True)
    email = db.Column(db.String(127), index=True, unique=True)
    password_hash = db.Column(db.String(127))
    
    def __repr__(self):
        return '<User {}{}{}>'.format(self.id, self.username,self.email)