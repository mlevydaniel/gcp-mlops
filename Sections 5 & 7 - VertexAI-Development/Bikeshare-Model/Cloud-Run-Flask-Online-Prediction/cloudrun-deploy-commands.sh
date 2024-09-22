# Grant the necessary permissions to the cloud run Service Account : 
gcloud projects add-iam-policy-binding 936546808722 \
  --member serviceAccount:936546808722-compute@developer.gserviceaccount.com  \
  --role='roles/aiplatform.admin'

# Step-1
docker buildx build --platform linux/amd64 -t bikeshare-online-predict .

# Push to Container Registry 
docker tag bikeshare-online-predict us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/bikeshare-online-predict
docker push us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/bikeshare-online-predict

gcloud run deploy bikeshare-online-predict --image  us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/bikeshare-online-predict --region us-central1
