print("beginning to run flask function file")
import numpy as np
import pandas as pd
#from matplotlib import pyplot as plt
from PIL import Image
from resizeimage import resizeimage
import os
#import re
import flask
#import json
from werkzeug import secure_filename
from scipy.misc import imread
from flask import render_template, send_from_directory, url_for
from . import app, original_dim, batch_size, symbol_df # , clf, graph
print("all package import done")

# GET request to the page http://127.0.0.1:5000/
@app.route("/")
def index():
    resultpath = "result"
    print('Aloha there! Index.html is rendering')
    return render_template('index.html', resultpath=resultpath)
print("index.html rendering function defined")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    print(filename)
    mydir = "../" + app.config['UPLOAD_FOLDER']
    return send_from_directory(mydir, filename)
print("file upload function defined")

# POST request
@app.route("/result", methods=["POST"])
def get_hieroglyph_info():
    pngfile = flask.request.files['file']
    filename = secure_filename(pngfile.filename)
    imgpath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    pngfile.save(imgpath)

    resized_filename = "resized_" + filename
    resized_imgpath = os.path.join(app.config['UPLOAD_FOLDER'], resized_filename)

    with Image.open(imgpath) as img:
        resized = resizeimage.resize_cover(img, original_dim)
        resized.save(resized_imgpath, img.format)

    imgpath_forhtml = str(url_for('uploaded_file', filename=filename))
    print(imgpath_forhtml)

    # convert image to np array
    # note: must be the same how train data was preprocessed
    # TODO: is it okay it's not png??
    arrayfile = imread(resized_imgpath, flatten = True, mode = "RGB").astype('float32')
    arrayfile = np.array([arrayfile for i in range(batch_size)])
    arrayfile = np.reshape(arrayfile, (batch_size, 1) + (original_dim)) / 255.

    # get prediction
    global graph
    # TODO slug size too big for Heroku, fix it and pred with real model
    # with graph.as_default():
    #     pred_array = clf.predict(arrayfile, batch_size = batch_size)
    # pred_cat = np.argmax(pred_array, 1)[0]
    pred_cat = 128 # hardcode placeholder
    cond = symbol_df["symbol_num"] == pred_cat
    pred = list(symbol_df.loc[cond, "symbol"])[0]
    desc = list(symbol_df.loc[cond, "translation"])[0]
    phonetic = list(symbol_df.loc[cond, "phonetic"])[0]
    freq_cat = list(symbol_df.loc[cond, "freq_cat"])[0]
    print("Prediction", pred)
    # flask.jsonify(pred)

    return render_template('result.html', imgpath = imgpath_forhtml, pred = pred, desc = desc, phonetic = phonetic, freq_cat = freq_cat)
print("result.html rendering function defined")

# For local development:
# app.run(debug=True)

# For public web serving:
# app.run(host='0.0.0.0')
