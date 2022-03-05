"""
Simple webhook app used to take in alerts sent from the Meraki cloud and post interesting data to a Webex Teams room. 
For local development, you will need to run a service to expose your app publicly (i.e. ngrok [https://ngrok.com/] or 
localtunnel [https://localtunnel.github.io/www/]), so that Meraki can reach your server. Otherwise, you can deploy this 
app on-prem or in a public cloud (AWS, Azure, GCP, etc.) and make sure that the instance is publicly accessible.
"""
from flask import Flask, request
import requests
import json
import os

# Environment variables to secure tokens, room IDs, etc.
try:
    WEBEX_BOT_TOKEN = os.environ.get("WEBEX_BOT_TOKEN")
    WEBEX_ROOM_ID = os.environ.get("WEBEX_ROOM_ID")
    MERAKI_VALIDATOR_STRING = os.environ.get("MERAKI_VALIDATOR_STRING")
except KeyError:
    raise Exception("Required environment variables are not set!")

# Initialize Flask app
app = Flask(__name__)

# Route to return validator string to Meraki - used to verify endpoint
@app.route("/", methods=["GET"])
def validator():
    """
    Used to validate endpoint with Meraki cloud
    """
    return MERAKI_VALIDATOR_STRING


# Route for Meraki event data
@app.route("/", methods=["POST"])
def data_intake():
    """
    Perform the following:
    - Take in data from Meraki
    - Validate the secret
    - Parse interesting data to be sent to user
    - Send interesting data to Webex Teams
    """
    if request.method == "POST":
        # Debugging purposes
        print("Data received from Webhook is: ", request.json)

        # Collect Meraki JSON data
        response = request.json

        # Parsing out interesting data from Meraki alert data and marking down for Webex payload
        webex_message = f"""
        ALERT: Network {response['networkName']} in organization {response['organizationName']} had the following change occur: 
        ```
        {response['alertData']}
        ```
        """

        # Base URL to post messages to Webex
        webex_url = "https://webexapis.com/v1/messages"

        # Payload for Webex Messages API
        message_body = json.dumps({"roomId": WEBEX_ROOM_ID, "markdown": webex_message})

        # Required headers for Webex Messages API call
        webex_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {WEBEX_BOT_TOKEN}",
        }

        # Send parsed data to Webex Teams room
        webex_post = requests.post(
            url=webex_url, headers=webex_headers, data=message_body, verify=False
        )

        # Print out response body and status code
        print(webex_post.status_code)
        print(webex_post.json())

        # Indicate whether request was successful (should be a log message)
        if webex_post.ok:
            print("Webex message sent!")
        else:
            print("Error sending to Webex")

        return "Webhook received!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
