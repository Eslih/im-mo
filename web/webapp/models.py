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


class Bribe(db.Model):
    __tablename__ = 'bribes'
    id = db.Column(db.Integer, primary_key=True)
    student = db.Column(db.String, nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    points = db.Column(db.Integer, nullable=False)

    def __init__(self, student, amount, points):
        self.student = student
        self.amount = amount
        self.points = points

    def __repr__(self):
        return '<Bribe {}>'.format(self.student)
