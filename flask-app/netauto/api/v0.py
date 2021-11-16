from flask import Blueprint

api_v0 = Blueprint("api_v0", __name__, url_prefix="/api/v0")

@api_v0.route("/")
def api_root():
    return {"api": {"version": "0",
                    "ping": "pong"}}
