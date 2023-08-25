import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from data.data import get_data, data


def predictions_linear_regression():
    # Create your dataset
    df = get_data(data)
    # Extract features and target
    X = df[["distancetravelled", "speed"]]
    y = df["fuelreading"]
    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Create and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    # Make predictions
    predictions = model.predict(X_test)
    print(predictions)
    # Calculate Mean Squared Error
    #mse = mean_squared_error(y_test, predictions)
    return predictions

predict = predictions_linear_regression()

