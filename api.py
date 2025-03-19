import os
import mlflow
from fastapi import FastAPI
from pydantic import BaseModel

MODEL_NAME = "my_sklearn_model"
MODEL_STAGE = "Production" 

app = FastAPI()

class PredictionRequest(BaseModel):
    feature1: float
    feature2: float
    # Add additional features as needed

@app.on_event("startup")
def load_model():
    global model
    try:
        tracking_uri = os.environ.get("MLFLOW_TRACKING_URI", "http://mlflow:5000")
        mlflow.set_tracking_uri(tracking_uri)
        model_uri = f"models:/my_sklearn_model/Production"
        model = mlflow.pyfunc.load_model(model_uri)
        print(f"Loaded model: {model_uri}")
    except Exception as e:
        print(f"Error loading model: {e}")
        # For testing, assign a dummy model so FastAPI stays alive.
        model = lambda x: [0]

@app.get("/")
def root():
    return {"message": "Welcome to the MLflow-FastAPI prediction service!"}

@app.post("/predict")
def predict(request: PredictionRequest):
    data = [[request.feature1, request.feature2]]
    prediction = model.predict(data)
    return {"prediction": prediction[0]}