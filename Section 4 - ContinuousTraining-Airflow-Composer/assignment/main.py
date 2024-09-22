import pandas as pd
from flask import Flask, request, jsonify
import joblib
import os, json
from google.cloud import storage
from google.cloud import logging
import logging as log
from google.oauth2 import service_account

app = Flask(__name__)
model = None

# credentials = service_account.Credentials.from_service_account_file('dataanalytics-347914-fd6f7b46fd46.json')

logging_client = logging.Client()
logger = logging_client.logger('advertising-roi-prediction-serving-logs')

storage_client = storage.Client()

def load_model():
    model = joblib.load("advertising_roi_model.joblib")
    return model

log.basicConfig(level=log.DEBUG)  # Changed to DEBUG for more verbose logging

def load_model_cloud():
    bucket_name = "gcs-mlops"
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob("advertising_roi/artifact/advertising_roi_model.joblib")
    blob.download_to_filename("advertising_roi_model.joblib")
    model = joblib.load("advertising_roi_model.joblib")
    return model


# load_model_cloud()
model = load_model_cloud()


@app.route('/predict', methods=['POST'])
def predict():
    try :
        input_json = request.get_json()
        logger.log_struct({
            'keyword': 'advertisement_roi_prediction_serving',
            'prediction_status': 1,
            'error_msg': input_json
        })

        input_df = pd.DataFrame(input_json, index=[0])
        y_predictions = model.predict(input_df)
        response = {'predictions': y_predictions.tolist()}

        logger.log_struct({
            'keyword': 'advertisement_roi_prediction_serving',
            'prediction_status': 1,
            'predicted_output': y_predictions
        })

        return jsonify(response), 200

    except Exception as e:
        logger.log_struct({
            'keyword': 'advertisement_roi_prediction_serving',
            'prediction_status': 0,
            'error_msg': str(e)
        })
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
