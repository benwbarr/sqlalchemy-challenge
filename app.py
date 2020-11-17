# 1. import Flask
from flask import Flask
import datetime as dt
import numpy as np
import pandas as pd

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
                      
Measurement = Base.classes.measurement
Station = Base.classes.station

# Session
session = Session(engine)

# Flask Setup
app = Flask (__name__)
                       
# Flask Routes
@app.route("/")
def welcome():
    return (
        f"All available API routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>")                     