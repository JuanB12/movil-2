from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/parcialfinal"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

app.secret_key = "parcial_final"

db = SQLAlchemy(app)

ma = Marshmallow(app)