from datetime import datetime

from flask import Flask, redirect, render_template, request, url_for
from flask_migrate import Migrate

from .config import get_database_url
from .models import Shipment, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = get_database_url()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

# Auto-init DB and sample data
with app.app_context():
    db.create_all()
    if Shipment.query.count() == 0:
        from .sample_data import populate_sample_data

        populate_sample_data()


@app.route("/")
def index():
    shipments = Shipment.query.all()
    return render_template("index.html", shipments=shipments)


@app.route("/shipment/<int:shipment_id>")
def shipment_detail(shipment_id):
    shipment = Shipment.query.get_or_404(shipment_id)
    return render_template("shipment_detail.html", shipment=shipment)


@app.route("/add_shipment", methods=["GET", "POST"])
def add_shipment():
    if request.method == "POST":
        tracking_number = request.form.get("tracking_number")
        recipient = request.form.get("recipient")
        address = request.form.get("address")
        status = request.form.get("status")
        last_updated = datetime.now()
        if tracking_number and recipient and address and status:
            db.session.add(
                Shipment(
                    tracking_number=tracking_number,
                    recipient=recipient,
                    address=address,
                    status=status,
                    last_updated=last_updated,
                )
            )
            db.session.commit()
            return redirect(url_for("index"))
    return render_template("add_shipment.html")


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
