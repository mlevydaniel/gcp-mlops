from flask import Flask, request, jsonify
from google.cloud import aiplatform

app = Flask(__name__)


def predict_instance(project_id, endpoint_id, instance):
    endpoint = aiplatform.Endpoint('projects/{}/locations/us-central1/endpoints/{}'.format(project_id, endpoint_id))
    instances_list = [instance]
    prediction = endpoint.predict(instances_list)
    return prediction


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    instance = data['instance']
    endpoint_id = 7110829768873869312
    project_id = 936546808722
    prediction = predict_instance(project_id, endpoint_id, instance)
    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# curl -X POST -H "Content-Type: application/json" -d '{"instance": [0.24, 0.81, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]}' https://bikeshare-online-predict-rhe2erspfa-uc.a.run.app/predict
