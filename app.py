import os
import json
from flask import Flask, send_file, request, redirect
from flask_admin import Admin, AdminIndexView
from flask.ext.admin.base import MenuLink, Admin, BaseView, expose
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
admin = Admin(app, name='Database', template_mode='bootstrap3', index_view=AdminIndexView(name='Index'))

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

class Demand(Base):
    __tablename__ = 'Demand'

    id = Column(Integer, primary_key=True)
    period = Column(Integer)
    demand = Column(Integer)
    week = Column(Integer)


### Route
@app.route("/")
def index():
    return send_file('front_end/dist/index.html')

@app.route("/api/create/seasonal_schedule", methods=['POST'])
def api_create_seasonal_schedule():
    import Schedule_switcher_demo as SS

    [WAs, WAm] = SS.main()
    numS = len(WAs)
    numM = len(WAm)

    for i in range(numS):
        for j in range(len(WAs[i])):
            if WAs[i, j] != 0:
                record = Seasonal_schedule(i+1, j+1, WAs[i, j])
                session.add(record)

    for i in range(numM):
        for j in range(len(WAm[i])):
            if WAm[i, j] != 0:
                record = Seasonal_schedule(numS+i+1, j+1, WAm[i, j])
                session.add(record)
    
    session.commit()
    return "success", 200




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
    return send_file('linechart.json')

@app.route("/api/database/ganttchart")
def api_ganttchart():
    return send_file('gantt.json')

@app.route("/api/create/daily_schedule", methods=['POST'])
def api_create_daily_schedule():
    pass

@app.route("/api/import/csv/demand", methods=['POST'])
def api_import_csv():
    if request.method == 'POST':
        print 'uploading CSV'
        request.files['upload'].save("uploads/demand.csv")
        return redirect("/admin")
    return redirect("/admin")

    ### testing API
# @app.route("/api/database/test")
# def db_test():
    # rows = session.query(Flight).all()
    # rows = str(rows[0])
    # print rows
    # return json.dumps([{"name": "Moroni", 'age': 50}, {'name':"Daniel", 'age': 22}, {'name': "No", 'age': 10}])

if __name__ == "__main__":
    admin.add_view(ModelView(Flight, session))
    admin.add_view(ModelView(Seasonal_schedule, session))
    admin.add_view(ModelView(Daily_schedule, session))
    admin.add_view(ModelView(Demand, session))
    admin.add_link(MenuLink(name='Back Home', url='/'))
    Base.metadata.create_all(engine)
    app.run(debug=True)
