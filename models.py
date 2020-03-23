from app import db
from sqlalchemy.dialects.postgresql import JSON

class Account(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username, password ):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)