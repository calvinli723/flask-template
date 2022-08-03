from app import db
from datetime import datetime

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Item {}".format(self.date)
