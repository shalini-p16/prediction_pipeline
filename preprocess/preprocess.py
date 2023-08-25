import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder


def label_encoder(df, vehicle_id, new_colname):
    label_encoder = LabelEncoder()
    df[new_colname] = label_encoder.fit_transform(df[vehicle_id])
    df.drop(columns=["vehicle_id"], inplace=True)
    return df


def drop_empty_columns(df):
    for col_name in df.columns:
        if df[col_name].notna().sum() == 0:
            df.drop(col_name, axis=1, inplace=True)
    return df


def preprocess(dataframe, colname):
    dataframe.drop(colname, axis=1, inplace=True)
    return dataframe


# Correlation feature selection
def feature_selection(data):
    # Feature selection
    features = ['fuelreading', 'distancetraveled', 'speed']
    target = 'target_variable'
    X = data[features]
    y = data[target]
    return X, y


def select_features_by_correlation(data, target_column, threshold=0.1):
    corr_matrix = data.corr()
    target_correlation = corr_matrix[target_column].abs().sort_values(ascending=False)
    selected_features = target_correlation[target_correlation > threshold].index.tolist()

    # Remove the target variable from selected features
    selected_features.remove(target_column)
    X = data[selected_features]
    y = data[target_column]

    return selected_features, X, y


def normalize_continuous_variables(df):
    non_numeric_columns = ['vehicle_id', 'timestamp']
    numeric_columns = [col for col in df.columns if col not in non_numeric_columns]

    df[numeric_columns] = normalize_continuous_variables(df[numeric_columns])
    df[numeric_columns]


def preprocess_data_for_lstm(data):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)
    X = []
    y = []
    for i in range(len(scaled_data) - 1):
        X.append(scaled_data[i:i + 1])
        y.append(scaled_data[i + 1:i + 2])
    X = np.array(X)
    y = np.array(y)

    return X, y
