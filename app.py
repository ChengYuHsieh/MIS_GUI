import os
import json
from flask import Flask
from flask import send_file
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

### setting static folder
STATIC_FOLDER = os.path.join(os.getcwd(), 'front_end/dist')

app = Flask(__name__, static_folder=STATIC_FOLDER, static_url_path='')
app.secret_key = "super secret key"
admin = Admin(app, name='Database', template_mode='bootstrap3')

### temporary allow CORS, should remove on production
from flask.ext.cors import CORS
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
###

### connecting database
engine = create_engine('postgresql://daniel:daniel@localhost/CI')
connection = engine.connect()

### declare mapping
Base = declarative_base()

### create database session
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

### Models
class Flight(Base):
    __tablename__ = 'flights'

    id = Column(Integer, primary_key=True)
    flightNum = Column(String(64))
    airline = Column(String(64))
    terminal = Column(String(64))
    counter = Column(Integer)
    gate = Column(String(64))

    def __init__(self, flightNum="", airline="", terminal="", counter=0, gate=""):
        self.flightNum = flightNum
        self.airline = airline
        self.terminal = terminal
        self.counter = counter
        self.gate = gate

    def __repr__(self):
        return "<Flight('%s', '%s', '%s', '%s', '%s')>" % (
                self.flightNum, self.airline, self.terminal, self.counter, self.gate)


# class Employee(Base):
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(64), unique=True)
    # email = db.Column(db.String(128))


### Route
@app.route("/")
def index():
    return send_file('front_end/dist/index.html')

@app.route("/api/database/test")
def db_test():
    rows = session.query(Flight).all()
    rows = str(rows[0])
    print rows
    return json.dumps([{"name": "Moroni", 'age': 50}, {'name':"Daniel", 'age': 22}, {'name': "No", 'age': 10}])


if __name__ == "__main__":
    admin.add_view(ModelView(Flight, session))
    Base.metadata.create_all(engine)
    app.run(debug=True)
