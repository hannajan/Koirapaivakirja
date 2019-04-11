from application import db


class Walk(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime)
    place = db.Column(db.String(120))
    length = db.Column(db.Float)

def __init__(self, start, end, place, length):
    self.start = start
    self.end = end
    self.place = place
    self.length = length

class WalkHandler(db.Model):
    walk_id = db.Column(db.Integer, db.ForeignKey('walk.id'), primary_key=True, nullable = False)
    handler_id = db.Column(db.Integer, db.ForeignKey('handler.id'), primary_key=True, nullable = False)

def __init__(self, walk_id, handler_id):
    self.walk_id = walk_id
    self.handler_id = handler_id