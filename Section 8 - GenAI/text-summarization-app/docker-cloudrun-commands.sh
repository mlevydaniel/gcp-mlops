# Step-1
docker buildx build --platform linux/amd64 -t llm-summarize-word-docs .

# Push to Container Registry 
docker tag llm-summarize-word-docs us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/llm-summarize-word-docs
docker push us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/llm-summarize-word-docs

gcloud run deploy llm-summarize-word-docs --image us-central1-docker.pkg.dev/dataanalytics-347914/python-apps/llm-summarize-word-docs --region us-central1
