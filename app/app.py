import flask
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True


import routes

if __name__ == "__main__":
    app.run(debug=True)
