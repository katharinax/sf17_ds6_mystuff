print("beginning of init")
import logging
import numpy as np
import pandas as pd
#from keras.models import load_model
#import tensorflow as tf
import pickle
from flask import Flask

original_dim = (75, 50)
batch_size = 32 # need to be exactly the same as training

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
print("begin to import pickled model and dictionary")
# clf = load_model('models/clf.h5')
        # TODO slug size too big for Heroku
        # deleted tf, keras, h5py from requirement.txt for now
# graph = tf.get_default_graph()
with open("models/dict.pkl", "rb") as pfile:
    symbol_df = pickle.load(pfile)

print("begin to import flask function file")
from .egypt_classifier import *   # flake8: noqa
print("finished init file")
