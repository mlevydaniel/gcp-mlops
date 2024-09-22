# Create a New Service Account in GCP before executing the below gcloud commands    
gcloud projects add-iam-policy-binding dataanalytics-347914 \
    --member=serviceAccount:vertexai-sa@dataanalytics-347914.iam.gserviceaccount.com \
    --role=roles/aiplatform.customCodeServiceAgent

gcloud projects add-iam-policy-binding dataanalytics-347914 \
    --member=serviceAccount:vertexai-sa@dataanalytics-347914.iam.gserviceaccount.com \
    --role=roles/aiplatform.admin

gcloud projects add-iam-policy-binding dataanalytics-347914 \
    --member=serviceAccount:vertexai-sa@dataanalytics-347914.iam.gserviceaccount.com \
    --role=roles/storage.objectAdmin
