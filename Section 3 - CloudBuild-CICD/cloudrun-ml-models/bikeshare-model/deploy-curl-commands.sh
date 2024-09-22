# Run the below curl cmd locally against your flask app running on PORT 8080
curl -X POST http://127.0.0.1:8080/predict \
-H "Content-Type: application/json" \
-d '{"temp":0.24,"humidity":0.81,"season_2":0,"season_3":0,"season_4":0,"month_2":0,"month_3":0,"month_4":0,"month_5":0,"month_6":0,"month_7":0,"month_8":0,"month_9":0,"month_10":0,"month_11":0,"month_12":0,"hour_1":0,"hour_2":0,"hour_3":0,"hour_4":0,"hour_5":0,"hour_6":0,"hour_7":0,"hour_8":0,"hour_9":0,"hour_10":0,"hour_11":0,"hour_12":0,"hour_13":0,"hour_14":0,"hour_15":0,"hour_16":0,"hour_17":0,"hour_18":0,"hour_19":0,"hour_20":0,"hour_21":0,"hour_22":0,"hour_23":0,"holiday_1":0,"weekday_1":0,"weekday_2":0,"weekday_3":0,"weekday_4":0,"weekday_5":0,"weekday_6":1,"workingday_1":0,"weather_2":0,"weather_3":0,"weather_4":0}'

# Build and push the docker image to GCP artifact registry

docker build -t bike_share_model_inference .

docker tag bike_share_model_inference us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/bike_share_model_inference

docker push us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/bike_share_model_inference

gcloud run deploy bikeshare-model-inference --image us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/bike_share_model_inference --region us-central1

# Submit your cloudbuild.yaml file 
gcloud builds submit --region us-central1

# Test cloud-run app after deployment 
curl -X POST https://bike-share-model-inference-rhe2erspfa-uc.a.run.app/predict \
-H "Content-Type: application/json" \
-d '{"temp":0.24,"humidity":0.81,"season_2":0,"season_3":0,"season_4":0,"month_2":0,"month_3":0,"month_4":0,"month_5":0,"month_6":0,"month_7":0,"month_8":0,"month_9":0,"month_10":0,"month_11":0,"month_12":0,"hour_1":0,"hour_2":0,"hour_3":0,"hour_4":0,"hour_5":0,"hour_6":0,"hour_7":0,"hour_8":0,"hour_9":0,"hour_10":0,"hour_11":0,"hour_12":0,"hour_13":0,"hour_14":0,"hour_15":0,"hour_16":0,"hour_17":0,"hour_18":0,"hour_19":0,"hour_20":0,"hour_21":0,"hour_22":0,"hour_23":0,"holiday_1":0,"weekday_1":0,"weekday_2":0,"weekday_3":0,"weekday_4":0,"weekday_5":0,"weekday_6":1,"workingday_1":0,"weather_2":0,"weather_3":0,"weather_4":0}'
