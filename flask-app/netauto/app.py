from flask import Flask
from netauto.api.v0 import api_v0

# Initialize the Flask app
app = Flask(__name__)

# Register the API blueprint
app.register_blueprint(api_v0)