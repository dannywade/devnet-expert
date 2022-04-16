from flask import Flask
from flask_restx import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

@api.route('/inventory/<string:device>')
class NetworkInventory(Resource):
    def __init__(self, device):
        parser = reqparse.RequestParser()
        parser.add_argument("device", type="string", help="Hostname of the network device")
        args = parser.parse_args()

    def get(self, device):
        return {'inventory': [{'name': device}]}
    
    def put(self, device):
        return 'Device added!', 201, {"Action": "Update"}

    def delete(self, device):
        return 'Device deleted!', 204, {"Action": "Delete"}



if __name__ == "__main__":
    app.run(debug=True)