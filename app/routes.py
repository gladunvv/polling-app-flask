from app import app
from flask import jsonify, abort, request
from tasks import example
from validators import MessageValidators


@app.route("/api/v1/sending_messages", methods=["POST"])
def sending_messages():
    data = request.json
    try:
        MessageValidators(data)
        message = {
            "message": "okkkk"
        }
        return message
    except:
        message = {
            "error": "invalid data"
        }
        return message


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