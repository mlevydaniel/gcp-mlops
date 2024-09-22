from google.cloud import aiplatform

PROJECT_ID = "dataanalytics-347914"
REGION = "us-central1"
aiplatform.init(project=PROJECT_ID, location=REGION)

job = aiplatform.PipelineJob(
    display_name='trigger-credit-scoring-pipeline',
    template_path="gs://udemy-gcp-mlops/mld-kubeflow-v1/credit-pipeline-deploy-v1.json",
    pipeline_root="gs://udemy-gcp-mlops/credit-pipeline-v1",
    enable_caching=False
)
job.submit()