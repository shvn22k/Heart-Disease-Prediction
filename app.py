
# from flask import Flask, render_template, request, jsonify
# import numpy as np
# import pickle

# app = Flask(__name__)
# model = pickle.load(open('heartDiseasePrediction.pkl', 'rb'))

# @app.route('/', methods=['GET'])
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         data = request.json  # Get JSON data from request
#         inputData = data['form_array']  # Retrieve form data
#         inputData = [float(x) for x in inputData]  # Convert to float
#         inputData = np.array(inputData).reshape(1, -1)

#         # Make the prediction using the loaded model
#         prediction = model.predict(inputData)
#         print(prediction)
#         if prediction[0] == "Presence":  # Assuming 1 means "Presence"
#             predicted_result = "You may have a heart disease. 😔"
#         elif prediction[0] == "Absence":
#             predicted_result = "You don't have a heart disease. 😊"
#         else:
#             predicted_result = "Error 🤖"

#         # Render the template with the prediction result
#         return jsonify(prediction_text=predicted_result)
#     else:
#         return jsonify(prediction_text="An error occurred. 🤖")

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify 
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('heartDiseasePrediction.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.json  # Get JSON data from request
        print(data)
        inputData = data['form_array']
        print(inputData)
        inputData = [float(x) for x in inputData] 
        print(inputData) # Convert to float
        inputData = np.array(inputData).reshape(1, -1)

        # Make the prediction using the loaded model
        prediction = model.predict(inputData)
        
        if prediction[0] == "Presence":  # Assuming 1 means "Presence"
            predicted_result = "You may have a heart disease. 😔"
        elif prediction[0] == "Absence":
            predicted_result = "You don't have a heart disease. 😊"
        else:
            predicted_result = "Error 🤖"

        # Return JSON response
        return jsonify(prediction_text=predicted_result)
    else:
        return jsonify(prediction_text="Error 🤖")

if __name__ == "__main__":
    app.run(debug=True)
