from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
import pyodbc
import os


app = Flask(__name__)
#
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.mysql')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)



class MLData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(20))
    location = db.Column(db.Integer)
    action = db.Column(db.String(40))
    timestamp = db.Column(db.String(40))
    date = db.Column(db.String(40))
    weekday = db.Column(db.String(40))
    holiday=db.Column(db.String(40))


def addData(user,location,action,timestamp,date,weekday,holiday):
	entry = MLData(user=user,location=location,action=action,timestamp=timestamp,date=date,weekday=weekday,holiday=holiday)
	db.session.add(entry)
	db.session.commit()

def getData():
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server= '+server + 
                      'Database=db.mysql;'
                      'Trusted_Connection=yes;')


    SQL_Query = pd.read_sql_query(
    '''select
    user,
    action,
    date,
    timestamp,
    location,
    holiday,
    weekday
    from MLData''', conn)