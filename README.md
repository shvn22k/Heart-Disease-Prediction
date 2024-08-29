# Heart Disease Prediction (90.78% Accuracy)

---  



**Heart Disease Prediction** project is an end-to-end machine learning project designed to predict the likelihood of heart disease using a classification algorithm. Built with Flask for the backend and Gaussian Naive Bayes for the machine learning model, this project demonstrates practical applications of data science and web development.

## Project Overview

This project leverages a pre-trained machine learning model to predict heart disease based on user inputs. The model is implemented using Gaussian Naive Bayes and is served through a Flask web application. The web interface allows users to input various health metrics and receive predictions on whether they might have heart disease.

### Features
- **Machine Learning Model**: Gaussian Naive Bayes
- **Backend**: Flask
- **Frontend**: HTML/CSS with static assets
- **Model Storage**: `.pkl` binary file
- **Deployment**: Render (for public access)
- **License**: MIT License

## Project Structure

- **`static/`**: Contains static files like images used in the application.
- **`templates/`**: Contains HTML templates, including `index.html`, which is the main user interface.
- **`heartDiseasePrediction.pkl`**: The serialized machine learning model.
- **`app.py`**: The Flask application that handles backend logic and serves the web application.
- **`requirements.txt`**: Lists Python dependencies for the project.

### Deployment
Deployed to web using render: [Deployment link](https://heart-disease-prediction-mcph.onrender.com/)

### Run locally
1. Download the repo and create a conda environment.
2. Do ```pip install -r requirements.txt```
3. Run the app using ```python run app.py``` in terminal

### Usage
- Input Your Data: Enter values for all fields in the form, including age, gender, chest pain type, blood pressure, cholesterol, and more. Ensure you select sensible and accurate values for each field.

- Submit the Form: Click the "PREDICT" button to get a prediction based on the provided inputs.

- View Results: The prediction will be displayed on the results section of the page.

### Notes
- Inputs: Make sure to enter **realistic values** for the best results. The application assumes sensible inputs for accurate predictions.
- Model Accuracy: The model's predictions are based on historical data and may not always reflect current health conditions. Current model accuracy is 90.78%.
- Site responsiveness: Site may be very slow due to inactivity on the site (as per free account hosting on render service).
- Jupyter notebook- The trained model was exported from my kaggle notebook which can be found here: [Heart Disease Prediction and EDA](https://github.com/shvn22k/kaggle-notebooks/blob/main/heart-disease-prediction.ipynb)

### License
This project is licensed under the MIT License. See the LICENSE file for details.


---  


