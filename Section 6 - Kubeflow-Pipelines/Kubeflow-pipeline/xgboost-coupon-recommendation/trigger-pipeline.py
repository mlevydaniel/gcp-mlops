from google.cloud import aiplatform

PROJECT_ID = "dataanalytics-347914"
REGION = "us-central1"
aiplatform.init(project=PROJECT_ID, location=REGION)

job = aiplatform.PipelineJob(
    display_name='trigger-coupon-model-pipeline',
    template_path="gs://udemy-gcp-mlops/mld-kubeflow-v1/coupon-pipeline.json",
    pipeline_root="gs://udemy-gcp-mlops/coupon-pipeline-v1",
    enable_caching=False
)
job.submit()
