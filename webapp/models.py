from datetime import datetime
from app import db

class User(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(60), index=True, unique=True)
     email = db.Column(db.String(100), index=True, unique=True)
     password_hash = db.Column(db.String(128))
     posts = db.relationship('Post', backref='author', lazy='dynamic')

    # def __repr__(self):
    # """
    #     tells Python how to print objects of this class
    # """
    #     return '<User {}>'.format(self.username)  

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)        