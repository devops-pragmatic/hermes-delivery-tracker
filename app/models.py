from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Sample(db.Model):
    """
    Example model for demonstration. Replace or extend for your assignment.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)


# --- Sample Delivery Tracker Models (for guidance only, do not implement) ---
# class Shipment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     tracking_number = db.Column(db.String(32), unique=True, nullable=False)
#     recipient = db.Column(db.String(128), nullable=False)
#     address = db.Column(db.String(256), nullable=False)
#     status = db.Column(db.String(32), nullable=False)
#     last_updated = db.Column(db.DateTime, nullable=False)
# --------------------------------------------------------------------------
