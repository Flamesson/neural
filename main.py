from flask import Flask, request, jsonify
from flask_restful import Api


app = Flask(__name__)
api = Api(app)


@app.route("/health/live", methods=["GET"])
def liveness():
    response = {"Status": "OK"}
    return jsonify(response)


@app.route("/health/ready", methods=["GET"])
def readiness():
    response = {"Status": "OK"}
    return jsonify(response)


@app.route("/size", methods=["POST"])
def process_image():
    image_data = request.data
    length = len(image_data)
    response = {"length": length}
    return jsonify(response)


if __name__ == '__main__':
    app.run()
