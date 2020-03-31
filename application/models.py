from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Account(UserMixin, db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username, password ):
        self.username = username
        self.set_password(password)
    def set_password(self, password):
         self.password = generate_password_hash(password, method='sha256')
    def check_password(self, password):
            """Check hashed password."""
            return check_password_hash(self.password, password)

    def __repr__(self):
        return '<id {}>'.format(self.id)