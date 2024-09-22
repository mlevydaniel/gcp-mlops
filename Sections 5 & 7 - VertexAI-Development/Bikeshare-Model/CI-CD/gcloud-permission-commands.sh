# Assign Service account user role to the service account 
gcloud projects add-iam-policy-binding dataanalytics-347914 \
--member=serviceAccount:936546808722@cloudbuild.gserviceaccount.com --role=roles/aiplatform.admin
# --member=serviceAccount:936546808722-compute@developer.gserviceaccount.com --role=roles/aiplatform.admin