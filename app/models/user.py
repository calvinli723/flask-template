from app import db, login
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    first_name =  db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    password_hash = db.Column(db.String(128))
    appointments = db.relationship("Appointment", backref="patient", lazy="dynamic")

    def __repr__(self):
        return "<User {}>".format(self.email)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))