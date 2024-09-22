# Step-1
docker buildx build --platform linux/amd64 -t advertising-app .

# Push to Artifact Registry 
docker tag advertising-app us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/advertising-app
docker push us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/advertising-app

# Deploy to Cloud Run
gcloud run deploy advertising-app \
--image us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/advertising-app \
--region us-central1 \
--allow-unauthenticated

# Run locally for testing
docker build -t advertising-app .
docker run -d -p 8080:8080 advertising-app