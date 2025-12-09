from flask import Flask, request,render_template
import numpy as np 
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Year =request.form['Year'] 
        average_rain_fall_mm_per_year =request.form['average_rain_fall_mm_per_year']  
        pesticides_tonnes=request.form['pesticide_tonnes']   
        Area=request.form['Area']
        Item=request.form['Item']
