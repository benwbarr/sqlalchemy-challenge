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