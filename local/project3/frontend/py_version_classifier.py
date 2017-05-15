#!/Users/katharina/anaconda/bin/python

import numpy as np
import pandas as pd
import re
from sklearn.ensemble import RandomForestClassifier
import pickle
import flask
import json

def tree_to_li(one_tree, featname_li, parent_index = None, direction = None):
    node = {}
    if direction == "l":
        node['name'] = int(one_tree.children_left[parent_index])
    elif direction == "r":
        node['name'] = int(one_tree.children_right[parent_index])
    else:
        node['name'] = 0
    n = int(one_tree.n_node_samples[node['name']])
    if one_tree.children_left[node['name']] != -1:
        feat_label = featname_li[one_tree.feature[node['name']]]
        thres = one_tree.threshold[node['name']]
        node['feat'] = feat_label + r" <= " + str(thres) + r" (n = " + str(n) + r")"
        node['children'] = [tree_to_li(one_tree, featname_li, node['name'], 'l'),
                            tree_to_li(one_tree, featname_li, node['name'], 'r')]
    else:
        node['feat'] = r"(n = " + str(n) + r")"
    return node

# import pickled data
with open('../backend/data_for_viz.pkl', 'rb') as picklefile:
    X = pickle.load(picklefile)
    y = pickle.load(picklefile)
    X_cols_label = pickle.load(picklefile)

rf = RandomForestClassifier()

# Initialize the app
app = flask.Flask(__name__)

# GET request to the page http://127.0.0.1:5000/
@app.route("/")
def hello():
    return "It's alive!!!"

# POST request
@app.route("/draw_tree", methods=["GET", "POST"])
def drawTree():

    # read the data that came with the POST request as a dict
    json_dict = flask.request.json
    which_tree = json_dict['treeparams'][0]

    # train model
    rf.fit(X, y)

    #produce tree json
    results = tree_to_li(rf[which_tree].tree_, X_cols_label)

    # Return a response with a json in it
    # flask has a quick function for that that takes a dict
    return flask.jsonify(results)


# Start the server, continuously listen to requests.
# We'll have a running web app!

# For local development:
app.run(debug=True)

# For public web serving:
# app.run(host='0.0.0.0')
