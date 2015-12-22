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


class Seasonal_schedule(Base):
    __tablename__ = 'seasonal_schedule'

    id = Column(Integer, primary_key=True)
    skillNum = Column(Integer)
    classNum = Column(Integer)
    numAssigned = Column(Integer)

    def __init__(self, skillNum=0, classNum=0, numAssigned=0):
        self.skillNum = skillNum
        self.classNum = classNum
        self.numAssigned = numAssigned

    def __repr__(self):
        return "<Seasonal_schedule('%s', '%s', '%s')>" % (
                self.skillNum, self.classNum, self.numAssigned)

class Daily_schedule(Base):
    __tablename__ = 'daily_schedule'

    id = Column(Integer, primary_key=True)
    schedule = Column(String(256))

    def __init__(self, schedule=''):
        self.schedule = schedule

    def __repr__(self):
        return "<Daily_schedule('%s')>" % (self.schedule)


### Route
@app.route("/")
def index():
    return send_file('front_end/dist/index.html')

@app.route("/api/create/seasonal_schedule")
def api__create_seasonal_schedule():
   pass 

@app.route("/api/database/seasonal_schedule")
def api_seasonal_schedule():
    data = []
    for row in session.query(Seasonal_schedule).order_by(Seasonal_schedule.id).all():
        data.append({
            'id': row.id,
            'skillNum': row.skillNum,
            'classNum': row.classNum,
            'numAssigned': row.numAssigned
        })
    return json.dumps(data)

@app.route("/api/database/daily_schedule")
def api_daily_schedule():
    data = []
    for row in session.query(Daily_schedule).order_by(Daily_schedule.id).all():
        data.append(json.loads(row.schedule))
    return json.dumps(data)

@app.route("/api/database/linechart")
def api_linechart():
    data = [
    ['data1', 30, 200, 100, 400, 150, 250],
    ['data2', 50, 20, 10, 40, 15, 25]
    ]
    return json.dumps(data)

### testing API
@app.route("/api/database/test")
def db_test():
    rows = session.query(Flight).all()
    rows = str(rows[0])
    print rows
    return json.dumps([{"name": "Moroni", 'age': 50}, {'name':"Daniel", 'age': 22}, {'name': "No", 'age': 10}])


if __name__ == "__main__":
    admin.add_view(ModelView(Flight, session))
    admin.add_view(ModelView(Seasonal_schedule, session))
    admin.add_view(ModelView(Daily_schedule, session))
    Base.metadata.create_all(engine)
    app.run(debug=True)
