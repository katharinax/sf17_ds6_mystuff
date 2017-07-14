print("beginning of init")
import logging
from sklearn.externals import joblib
import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd

from flask import Flask

# create logger for app
print("create logger for app")
logger = logging.getLogger('app')
logger.setLevel(logging.INFO)

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT)

print("beginning of app assignment")
app = Flask(__name__)
app.config.from_object("app.config")

# import pickled data/model
print("begin to import pickle")
with open('models/data_for_viz.pkl', 'rb') as picklefile:
    rf = pickle.load(picklefile)
    X_cols_label = pickle.load(picklefile)

print("begin to import the py file")
from .py_version_classifier import *   # flake8: noqa
print("finished init file")
