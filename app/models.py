from . import db
from werkzeug.security import (generate_password_hash, check_password_hash)
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

class Feedback(db.Model):

    __table__name = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    feedback_section = db.Column(db.Text)
    user_id =  db.Column(db.Integer, db.ForeignKey('users.id'))
    comments_id =  db.Column(db.Integer, db.ForeignKey('comments.id'))

class Comments(db.Model):

    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment_section = db.Column(db.Text)
    categories = db.Column(db.String)

    def __init__(self, comment_section, categories):
        self.comment_section = comment_section
        self.categories = categories

    def __repr__(self):
        return f"Take a look at this pitch, what do you think?: {self.comment_section}"


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'
