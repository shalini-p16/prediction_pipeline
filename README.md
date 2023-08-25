1 Introduction
The goal of a prediction pipeline is to streamline and automate the process of making
predictions from the data retrieved from the InfluxDB while ensuring consistency
and reproducibility. This project focusses on retrieving data for only one IoT device

1.1 Dataset
The following dataset has been taken for the machine learning model to make pre-
dictions. The dataset remains the same with following vehicle characteristics:
• Timestamp : The timestamp indicates the date and time when the fuel reading
was taken
• Vehicle Id : It represents unique id of each vehicle
• Fuel Reading : This is the measurement of the amount of fuel present in the
vehicle’s fuel tank at the time of reading
• Distance Travelled : This feature represents the distance the vehicle has trav-
eled since the last reading. Longer distances requires more fuel
• Speed : speed refers to the rate at which the vehicle is moving. It can impact
fuel consumption
1.2 Features of the Project
• Retrieves data from the database based on scheduler. Each IoT device data can
be collected by querying the database from measurement, tags and bucket
• Data is then preprocessed and transformed into the data which can be used by
different models
• Important features are extracted based on the machine learning model being
used
• The data is then split into train, test and validation set for model training ,
measuring the performance and predictions
• This result is then showed on the Flask UI based on the input from the user
2 Architecture
The architecture of a prediction pipeline involves multiple components working to-
gether to perform data processing, model training, and prediction. 

• Data Extraction : Data is extracted from the database using queries
• Preprocessing and Feature Extraction: Data is preprocessed to get the clean
data and relevant features are extracted
• Model Training: Preprocessed data is split into train data,test data and valida-
tion data, two models are then trained using this training data. Trained model
is then stored in the project path
• Prediction: Prediction result is generated using the test data
• Flask UI Based on the selected model, result is displayed on the UI
• Retraining New data retrieved from the database (based on scheduler) follows
the same process from data extraction to prediction of results
FIGURE 1: Project Architecture
3 Project Structure
 It has following components:
• app: app directory contains Flask UI code which accepts model type from a
drop down and predicts result based on the selection. It contains related html
and css files
• data : this directory contains code to retrieve data from the InfluxDB, scheduler
which retrieves new data based on time paramer and stores new data retrieved
from the database for further steps
• models: it holds the implementations of machine learning models xgboost and
linear regression
