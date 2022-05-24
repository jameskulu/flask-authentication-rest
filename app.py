from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


# Run server
if __name__ == '__main__':
    app.run(debug=True)