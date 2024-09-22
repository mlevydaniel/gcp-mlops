# Step-1
docker buildx build --platform linux/amd64 -t llm-text-classifcation .

# Push to Container Registry 
docker tag llm-text-classifcation us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/llm-text-classifcation
docker push us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/llm-text-classifcation


gcloud run deploy llm-text-classifcation --image us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/llm-text-classifcation --region us-central1