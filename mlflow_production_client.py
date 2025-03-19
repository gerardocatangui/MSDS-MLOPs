from mlflow.tracking import MlflowClient

client = MlflowClient()
client.transition_model_version_stage(
    name="my_sklearn_model",
    version=1,
    stage="Production"
)