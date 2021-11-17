from flask import Flask, render_template, request
from api.v0 import api_v0
from utils import get_ios_version

# Initialize the Flask app
app = Flask(__name__)

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
    host = request.form['hostname']
    host_version = get_ios_version(host)
    return render_template('show-version-results.html', hostname=host, version=host_version)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, use_reloader=True)