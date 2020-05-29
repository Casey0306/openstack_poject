from flask import Flask, request, jsonify, make_response
from functools import wraps
from connect_to_openstack_api import Openstackapi

app = Flask(__name__)

openstackapi = Openstackapi()


def token_check(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        if token != openstackapi.token:
            return jsonify({'message': 'Token is mismatch!',
                            "token": token, "opensatckapitoken": openstackapi.token}), 400

        if openstackapi.check_token_status() == 0:
            return jsonify({'message': 'Token is expired!'}), 401

        return f(*args, **kwargs)

    return decorated


@app.route('/login', methods=['GET'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401,
                             {'WWW-Authenticate': 'Basic realm="Login required!"'})

    openstackapi.token = ""
    response = openstackapi.auth_keystone(auth.username, auth.password)

    if openstackapi.token != "":
        return jsonify({"token": response}), openstackapi.status_code
    else:
        return make_response('Could not verify', 401,
                             {'WWW-Authenticate': 'Basic realm="Login required!"'})


@app.route('/flavors', methods=['GET'])
@token_check
def flavors():
    response = openstackapi.get_flavors()
    if openstackapi.status_code == 200:
        return jsonify(response), openstackapi.status_code
    else:
        return jsonify({"Error": "Error to get flavors"}), openstackapi.status_code


@app.route('/images', methods=['GET'])
@token_check
def images():
    response = openstackapi.get_images()
    if openstackapi.status_code == 200:
        return jsonify(response), openstackapi.status_code
    else:
        return jsonify({"Error": "Error to get images"}), openstackapi.status_code


@app.route('/networks', methods=['GET'])
@token_check
def networks():
    response = openstackapi.get_networks()
    if openstackapi.status_code == 200:
        return jsonify(response), openstackapi.status_code
    else:
        return jsonify({"Error": "Error to get networks"}), openstackapi.status_code


@app.route('/servers', methods=['GET'])
@token_check
def servers():
    response = openstackapi.get_vms()
    if openstackapi.status_code == 200:
        return jsonify(response), openstackapi.status_code
    else:
        return jsonify({"Error": "Error to get servers"}), openstackapi.status_code


@app.route('/server/<server_id>', methods=['GET'])
@token_check
def server(server_id):
    response = openstackapi.get_vm(server_id)
    if openstackapi.status_code == 200:
        return jsonify(response), openstackapi.status_code
    else:
        return jsonify({"Error": "Error to get servers"}), openstackapi.status_code


@app.route('/create_server', methods=['POST'])
@token_check
def create_server():
    data = request.get_json()
    response = openstackapi.create_vm(data["name"], data["image_id"],
                                      data["flavor_ref"], data["networks_id_list"])
    return jsonify({"status-code": response}), openstackapi.status_code


if __name__ == '__main__':
    app.run(debug=True)