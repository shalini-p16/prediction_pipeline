from flask import Flask, render_template, request
from models.linear_regression import predictions_linear_regression
from models.xgboost import *

app = Flask(__name__)

# Routing to the home page
@app.route('/')
def home():
    return render_template('index.html')

# Routing to the model predictions page
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        selected_model = request.form['selected_model']
        # Call the appropriate prediction model based on selected_model
        if selected_model == 'xgboost':
            predictions = xgboost_prediction(data)
        elif selected_model == 'linear':
            predictions = predictions_linear_regression()
        else:
            predictions = None
        return render_template('predictions.html', predictions=predictions)


if __name__ == '__main__':
    app.run(debug=True)
