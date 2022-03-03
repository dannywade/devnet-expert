"""
Simple script used to take in alerts sent from the Meraki cloud and pass interesting data to a Webex Teams room
"""
from flask import Flask

app = Flask(__name__)

@app.get("/")
def validator():
    """
    Used to validate endpoint with Meraki cloud
    """
    validator_str = ""
    return validator_str

@app.post("/")
def data_intake():
    """
    Perform the following:
    - Take in data from Meraki
    - Validate the secret
    - Parse interesting data to be sent to user
    - Send interesting data to Webex Teams
    """