import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestRegressor
from google.cloud import storage
from joblib import load
import os
import time
import logging

app = Flask(__name__)
model = None

storage_client = storage.Client()
bucket = storage_client.bucket("gcs-mlops")

logging.basicConfig(level=logging.INFO)


def one_hot_encoding(data, column):
    data = pd.concat([data, pd.get_dummies(data[column], prefix=column, drop_first=True)], axis=1)
    data = data.drop([column], axis=1)
    return data


def load_model():
    storage_client = storage.Client()
    bucket_name = "gcs-mlops"
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob("ml-artifacts/model.joblib")
    blob.download_to_filename("model.joblib")
    model = load(open("model.joblib", "rb"))
    return model

model = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    start_time = time.time()
    try :
        input_json = request.get_json()
        input_df = pd.DataFrame(input_json, index=[0])
        y_predictions = model.predict(input_df)

        prediction_time = time.time()
        logging.info(f"Time to predict: {prediction_time - start_time} seconds")

        response = {'predictions': y_predictions.tolist()}
        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
