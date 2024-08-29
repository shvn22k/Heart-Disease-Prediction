#import libraries
from flask import Flask, render_template, request, jsonify 
import numpy as np
import pickle

#make an app
app = Flask(__name__)
model = pickle.load(open('heartDiseasePrediction.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html') #render empty html page

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.json  # get JSON data from request
        print(data)
        inputData = data['form_array']
        print(inputData)
        inputData = [float(x) for x in inputData] 
        print(inputData) # convert to float
        inputData = np.array(inputData).reshape(1, -1)

        #make the prediction using the loaded model
        prediction = model.predict(inputData)
        
        if prediction[0] == "Presence":  
            predicted_result = "You may have a heart disease. 😔"
        elif prediction[0] == "Absence":
            predicted_result = "You don't have a heart disease. 😊"
        else:
            predicted_result = "Error 🤖"

        # return JSON response
        return jsonify(prediction_text=predicted_result)
    else:
        return jsonify(prediction_text="Error 🤖")

if __name__ == "__main__":
    app.run(debug=True)
