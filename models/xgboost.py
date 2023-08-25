from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import xgboost
from data.data import *
from data.data import get_data
from preprocess.preprocess import label_encoder, preprocess, normalize_continuous_variables, select_features_by_correlation

def build_xgboost_model():
    model = xgboost.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1)
    return model

def train_xgboost_model(X_train, y_train):
    model = build_xgboost_model()
    model.fit(X_train, y_train)
    return model

def predict_xgboost_model(model, X):
    predictions = model.predict(X)
    return predictions


def evaluate_and_display_results(predictions, actual):
    mse = mean_squared_error(actual, predictions)
    print(f"Mean Squared Error: {mse}")


def xgboost_prediction(df):
    raw_data = get_data(data)
    new_df = label_encoder(raw_data, "vehicle_id", "vehicle_encoded")
    print(new_df)

    processed_data = preprocess(new_df, "timestamp")
    print(processed_data)

    target_column = "fuelreading"
    selected_features, X, y = select_features_by_correlation(processed_data, target_column, threshold=0.1)
    print("Selected Features:", selected_features)
    print(X)

    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Train the XGBoost model
    xgboost_model = train_xgboost_model(X_train, y_train)

    # Make predictions
    predictions = predict_xgboost_model(xgboost_model, X_test)

    # Evaluate and display results
    #final_result = evaluate_and_display_results(predictions, y_test)
    print(predictions)


    return predictions

predict = xgboost_prediction(data)
