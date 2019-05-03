import datetime

from application import db
from sqlalchemy import text

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


    @staticmethod
    def count_walked_km_for_dog(dog_id):
        stmt = text("SELECT Dog.name, COUNT(Walk.length) FROM Walk"
                    " JOIN DogWalk ON DogWalk.walk_id = Walk.id"
                    " JOIN Dog ON Dog.id = DogWalk.dog_id"
                    " WHERE Dog.id = :dog_id;").params(dog_id=dog_id)

        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[0], "km":row[1]})

        return response