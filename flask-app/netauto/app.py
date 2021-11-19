from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from api.v0 import api_v0
from utils import get_ios_version
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)
# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize the DB object
db = SQLAlchemy(app)

# Model for the Device table
class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(50), unique=True, nullable=False)
    version = db.Column(db.String(20))
    date_created = db.Column(db.DateTime, default=datetime.now)

# Register the API blueprint
app.register_blueprint(api_v0)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/show-version")
def show_version():
    return render_template('show-version.html')

@app.route("/show-version-results", methods=["POST"])
def get_version_results():
    # Retrieve hostname from HTML form
    host = request.form['hostname']
    # Collect software version from queried device
    host_version = get_ios_version(host)

    # Store the captured device into the database for API use
    store_device_info = Device(hostname=host, version=host_version)
    db.session.add(store_device_info)
    db.session.commit()

    # Return HTML page with device hostname and discovered software version
    return render_template('show-version-results.html', hostname=host, version=host_version)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, use_reloader=True)