# Assign Service account user role to the service account 
gcloud projects add-iam-policy-binding dataanalytics-347914 \
  --member=serviceAccount:gcp-mlops@dataanalytics-347914.iam.gserviceaccount.com --role=storage.buckets.get

# Assign Cloud Run role to the service account 
gcloud projects add-iam-policy-binding dataanalytics-347914 \
  --member=serviceAccount:gcp-mlops@dataanalytics-347914.iam.gserviceaccount.com --role=roles/run.admin

gcloud projects add-iam-policy-binding dataanalytics-347914 \
    --member=serviceAccount:gcp-mlops@dataanalytics-347914.iam.gserviceaccount.com \
    --role=roles/storage.objectViewer

# Command to run the build using cloudbuild.yaml
gcloud builds submit --region us-central1

