from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy


import os, io
import uuid
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from base64 import b64encode


from PIL import Image
import requests
from io import BytesIO

import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.patches import Polygon

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'visionAPIkey.json'

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usrData.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    #title = 'Create the input'
    return render_template('index.html')#, title=title)

@app.route('/habitsDrag', methods=['GET', 'POST'])
def habitsDrag():
    #title = 'Create the input'
    return render_template('habitsDrag.html')#, title=title)

@app.route("/f", methods=["GET", "POST"])
def f():
    if request.method == "POST":
        print("ANALYSING")
        if request.files:
            image = request.files["image"]
            img = Image.open(image)
            imgProcessed = Image.open(io.BytesIO(analyse(img)))
            image_io = BytesIO()
            imgProcessed.save(image_io, 'PNG')
            dataurl = 'data:image/png;base64,' + b64encode(image_io.getvalue()).decode('ascii')
            return render_template('f.html', image_data=dataurl)

            return redirect(request.url)

    return render_template("f.html")

@app.route('/habits', methods=['GET', 'POST'])
def habits():
    if request.method == 'GET':
        print("GETTING")
        return render_template('habits.html')
    print("POSTING")
    global data
    data = request.get_data()
    print(type(data))
    #print(request.get_json())
    #print(request.json['imgDataJson'])
    #return render_template('analysis.html', data=data)
    return redirect(url_for('analysis'))

@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    img = request.files['imgInp']
    img = Image.open(BytesIO(img))
    analyse(img)
    if request.method == 'GET':
        print('rendering "analysis"')
        return render_template('analysis.html', data=data)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/ideas', methods=['GET'])
def ideas():
    return render_template('ideas.html')




@app.route('/results/<uuid>', methods=['GET'])
def results(uuid):
    title = 'Result'
    data = get_file_content(uuid)
    return render_template('layouts/results.html',
                           title=title,
                           data=data)

@app.route('/postmethod', methods = ['POST'])
def post_javascript_data():
    jsdata = request.form['canvas_data']
    unique_id = create_csv(jsdata)
    params = { 'uuid' : unique_id }
    return jsonify(params)

def analyse(img): 
    client = vision.ImageAnnotatorClient()

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # construct an iamge instance
    image = types.Image(content=img_byte_arr)
    response = client.text_detection(image=image)  # returns TextAnnotation


    texts = response.text_annotations

    fig = Figure()
    output = io.BytesIO()
    #plt.figure(figsize=(12, 20))
    #plt.imshow(img)
    for text in texts:    
        vertices = [[vertex.x, vertex.y] for vertex in text.bounding_poly.vertices]
        vertices.append(vertices[0]) #repeat the first point to create a 'closed loop'

        xs, ys = zip(*vertices) #create lists of x and y values
        plt.plot(xs,ys) 
    FigureCanvas(fig).print_png(output)
    return output.getvalue()#, mimetype='image/png')
    #plt.savefig()
    #plt.show() # if you need...


if __name__ == '__main__':
    app.run()
