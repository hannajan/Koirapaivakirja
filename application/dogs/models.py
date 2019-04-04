import datetime

from application import db

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    breed = db.Column(db.String(120), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

def __init__(self, name, breed, birthday):
    self.name = name
    self.breed = breed
    self.birthday = birthday