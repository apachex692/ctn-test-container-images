from os import getenv

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def helloworld():
    if request.method == "GET":
        data = {"data": "Hello World"}
        return jsonify(data)


@app.route("/create", methods=["POST"])
def create_data():
    if request.method == "POST":
        data = request.json
        response = {"message": "Data Created", "data": data}
        return jsonify(response)


@app.route("/update", methods=["PATCH"])
def update_data():
    if request.method == "PATCH":
        data = request.json
        response = {"message": "Data Updated", "data": data}
        return jsonify(response)


@app.route("/replace", methods=["PUT"])
def replace_data():
    if request.method == "PUT":
        data = request.json
        response = {"message": "Data Replaced", "data": data}
        return jsonify(response)


@app.route("/delete", methods=["DELETE"])
def delete_data():
    if request.method == "DELETE":
        response = {"message": "Data Deleted"}
        return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=getenv("FLASK_APP_PORT", 5000))
