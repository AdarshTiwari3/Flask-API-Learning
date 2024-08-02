from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"
class Car(db.Model):
    __tablename__ = 'car'
    car_id = db.Column(db.Integer, primary_key=True)
    model= db.Column(db.String(200), nullable=False)
    owner = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Car('{self.model}', '{self.owner}', '{self.year}')"