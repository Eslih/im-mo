from . import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    property = db.Column(db.String, nullable=False)
    amount = db.Column(db.Numeric(12), nullable=False)

    def __init__(self, property, amount):
        self.property = property
        self.amount = amount

    def __repr__(self):
        return '<Transaction {}>'.format(self.property)
