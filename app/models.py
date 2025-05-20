from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Shipment(db.Model):
    __tablename__ = "shipments"
    id = db.Column(db.Integer, primary_key=True)
    tracking_number = db.Column(db.String(32), unique=True, nullable=False)
    recipient = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    status = db.Column(db.String(32), nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False)
