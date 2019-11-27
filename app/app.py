import flask
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "it-is-secret-key"


@app.route("/api/v1/sending_messages", methods=["GET"])
def convert():
    data = {
        "Hello": "World"
    }
    return data

app.run(debug=True)