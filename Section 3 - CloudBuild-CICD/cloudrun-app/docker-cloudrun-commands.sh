# Step-1
docker buildx build --platform linux/amd64 -t demo-flask-app .


# Push to Container Registry 
docker tag demo-flask-app gcr.io/dataanalytics-347914/demo-flask-app
docker push gcr.io/dataanalytics-347914/demo-flask-app

gcloud run deploy demo-flask-app --image gcr.io/udemy-mlops-395416/demo-flask-app --region us-central1


# Push to Artifact Registry 
docker tag demo-flask-app us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/demo-flask-app
docker push us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/demo-flask-app

gcloud run deploy demo-flask-app \
--image us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/demo-flask-app \
--region us-central1


gcloud run deploy demo-flask-app \
--image us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/demo-flask-app \
--region us-central1 \
--service-account gcp-mlops@dataanalytics-347914.iam.gserviceaccount.com \
--allow-unauthenticated


# Run locally for testing
docker run -d -p 8080:8080 demo-flask-app
