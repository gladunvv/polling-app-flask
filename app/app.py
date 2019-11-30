import flask
from flask import jsonify, abort
import os

app = flask.Flask(__name__)
db = SQLAlchemy(app)

app.config["DEBUG"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route("/api/v1/sending_messages", methods=["GET"])
def sending_messages():
    data = {
        "Hello": "World"
    }
    return data


@app.errorhandler(400)
def bad_request_error(error):
    message = {
        "error": f"{error}",
    }
    return jsonify(message), 400


@app.errorhandler(500)
def internal_error(error):
    message = {
        "error": f"{error}",
    }
    return jsonify(message), 500


@app.errorhandler(405)
def method_not_allowed(error):
    message = {
        "error": f"{error}",
    }
    return jsonify(message), 500


@app.errorhandler(404)
def not_found_error(error):
    message = {
        "error": f"{error}",
    }
    return jsonify(message), 404


app.run(debug=True)