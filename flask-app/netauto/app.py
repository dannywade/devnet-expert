from flask import Flask, render_template, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from utils import get_ios_version
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)

# Configuration for SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Initialize the DB object
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for the Device table
class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(50), unique=True, nullable=False)
    version = db.Column(db.String(20))
    date_created = db.Column(db.DateTime, default=datetime.now)


# Schema for serialization/deserialization of data from database
class DeviceSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Device

    id = ma.auto_field()
    hostname = ma.auto_field()
    version = ma.auto_field()
    date_created = ma.auto_field()


# Instantiate schema classes to use in routes
device_schema = DeviceSchema()
devices_schema = DeviceSchema(many=True)


@app.route("/")
def index():
    return render_template("index.html")


# Presents form to user
@app.route("/show-version")
def show_version():
    return render_template("show-version.html")


# Form submittal to gather OS version from specified device
@app.route("/show-version-results", methods=["POST"])
def get_version_results():
    # Retrieve hostname from HTML form
    host = request.form["hostname"]
    # Collect software version from queried device
    host_version = get_ios_version(host)

    # Store the captured device into the database for API use
    store_device_info = Device(hostname=host, version=host_version)
    db.session.add(store_device_info)
    db.session.commit()

    # Return HTML page with device hostname and discovered software version
    return render_template(
        "show-version-results.html", hostname=host, version=host_version
    )


# API routes
# API root - used for testing
@app.route("/api/v0/")
def api_root():
    return {"api": {"version": "0", "ping": "pong"}}


# Gathers all records from the Devices table
@app.route("/api/v0/devices")
def get_all_devices():
    all_devices = Device.query.all()
    return devices_schema.jsonify(all_devices)


# Gets specific device based on the hostname found in the URI
@app.route("/api/v0/devices/<device_hostname>")
def get_one_device(device_hostname):
    one_device = Device.query.filter_by(hostname=device_hostname).first()
    return device_schema.jsonify(one_device)


# Gets specific device based on the ID found in the URI
@app.route("/api/v0/devices/id/<device_id>")
def get_device_by_id(device_id):
    one_device_by_id = Device.query.filter_by(id=device_id).first()
    return device_schema.jsonify(one_device_by_id)


# Gets all devices running a particular OS version
@app.route("/api/v0/devices/os-version/<os_version>")
def get_devices_by_os(os_version):
    devices_by_version = Device.query.filter_by(version=os_version).all()
    return devices_schema.jsonify(devices_by_version)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, use_reloader=True)
