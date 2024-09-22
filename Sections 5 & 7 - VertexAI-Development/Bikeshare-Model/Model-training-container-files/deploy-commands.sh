
# Step-1 - Build the image 
docker buildx build --platform linux/amd64 -t vertex-bikeshare-model .

# Step-2 - Tag the image locally
docker tag vertex-bikeshare-model us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/vertex-bikeshare-model

# Step-3 - Push the image to Google Cloud Registry 
docker push us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/vertex-bikeshare-model

# Step-4 - Submit a custom model training job  
gcloud ai custom-jobs create --region=us-central1 \
--project=dataanalytics-347914 \
--worker-pool-spec=replica-count=1,machine-type='n1-standard-4', container-image-uri='us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/vertex-bikeshare-model' \
--display-name=bike-sharing-model-training