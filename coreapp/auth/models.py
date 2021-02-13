from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from coreapp import db

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(256), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    fname = db.Column(db.String(256))
    lname = db.Column(db.String(256))
    phone = db.Column(db.String(25))
    img = db.Column(db.String(128))
    signup_date = db.Column(db.String(128))
    projects = db.relationship('Project', backref='author', lazy=True)
    collaborations = db.relationship('CollaboratorProject', back_populates='collaborator')

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()