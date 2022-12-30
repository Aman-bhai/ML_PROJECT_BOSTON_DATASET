import pickle
from flask import Flask,request,app,jsonify,url_for,render_template,redirect,flash
import numpy as np
import pandas as pd

app=Flask(__name__)
model=pickle.load(open('regression_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict.api',methods=['POST'])

def predict_api():
    data=request.json['data']
    print(data)
    