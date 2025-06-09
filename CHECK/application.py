from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pf
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application


ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "POST":
        Temperature = float(request.form.get("Temperature"))
        RH = float(request.form.get("RH"))
        Ws = float(request.form.get("Ws"))
        Rain = float(request.form.get("Rain"))
        FFMC = float(request.form.get("FFMC"))
        DMC = float(request.form.get("DMC"))
        ISI = float(request.form.get("ISI"))
        Classes = int(request.form.get("Classes"))
        Region = int(request.form.get("Region"))

        # Arrange the input in the format expected by the model
        input_data = [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]

        # Scale and predict
        scaled_data = standard_scaler.transform(input_data)
        prediction = ridge_model.predict(scaled_data)

        # Send the result to the template
        return render_template('home.html', result=prediction[0])
    
    else:
        return render_template('home.html', result=None)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
