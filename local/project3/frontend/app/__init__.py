import logging
from sklearn.externals import joblib
import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd

from flask import Flask

# create logger for app
logger = logging.getLogger('app')
logger.setLevel(logging.INFO)

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT)

app = Flask(__name__)
app.config.from_object("app.config")

# import pickled data/model
with open('models/data_for_viz.pkl', 'rb') as picklefile:
    rf = pickle.load(picklefile)
    X_cols_label = pickle.load(picklefile)

from .py_version_classifier import *   # flake8: noqa
