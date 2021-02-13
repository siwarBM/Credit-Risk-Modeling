
#from flask import Flask, render_template, request

from flask import Flask,render_template,url_for,request
from flask import render_template,request,jsonify
import numpy as np
import pandas as pd
import re
import pickle
import string
from sklearn import model_selection
import lightgbm as lgb 
import requests
# Create an app object

filename= 'Risk_modelGBM (1).pkl'
app = Flask(__name__)
#load the model from disk
model=pickle.load((open(filename,'rb')))

app = Flask(__name__)
@app.route('/')
def home():
	return render_template('home.html')
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender=int(request.form['Gender'])
        age = int(request.form['age'])
        car=int(request.form['car'])
        annual_income=float(request.form['annual_income'])
        family_status=int(request.form['family_status'])
        house=int(request.form['house'])
        employement= float(request.form['employement'])
        fam_members=float(request.form['fam_members'])
        c=int(request.form['c'])
        if (( annual_income > 170000) and c==1):
            class1=1
            class3=0
            class2=0
            others=0
        elif ((annual_income < 150000)and c==1):
            class1=0
            class3=1
            class2=0
            others=0
        elif ((175000>annual_income>155000)and c==1):
            class1=0
            class3=0
            class2=1
            others=0
        elif (c==1):
            class1=0
            class3=0
            class2=0
            others=1
        else:
            class1=0
            class3=0
            class2=0
            others=0
    arr = np.array([[Gender,age,car,annual_income,class1,class2,class3,others,family_status,house,employement,fam_members]])
   
    
  
    pred =model.predict(arr)
    return render_template('result.html',prediction = pred[0])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int("3060"),debug=True)
                  