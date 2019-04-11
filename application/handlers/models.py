from application import db

class Handler(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    
    walkhandlers = db.relationship("WalkHandler", backref='handler', lazy=True)


    def __init__(self, name):
        self.name = name