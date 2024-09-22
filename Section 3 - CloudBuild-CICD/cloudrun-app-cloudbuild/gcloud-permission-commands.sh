# Assign Service account user role to the service account 
gcloud projects add-iam-policy-binding dataanalytics-347914 \
--member=serviceAccount:936546808722@cloudbuild.gserviceaccount.com --role=roles/iam.serviceAccountUser


# Assign Cloud Run role to the service account 
gcloud projects add-iam-policy-binding dataanalytics-347914 \
  --member=serviceAccount:936546808722@cloudbuild.gserviceaccount.com --role=roles/run.admin
