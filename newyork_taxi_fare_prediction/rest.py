"""module for API for calling models"""

from typing import Dict
from fastapi import FastAPI
import torch

# Creating an instance of App
app = FastAPI()

# Get model for model calls

@app.get("/")
def get_predictions(model_feature_values: torch.Tensor) -> Dict:
    """endpoint for model price prediction"""

    # TODO:- Load the saved model
    # TODO:- Get predictions from model
    # TODO:- Return predictions as a JSON object
    model_feature_values = None
    if model_feature_values is None:
        return {'message': torch.Tensor([500])}
    return {'message': torch.Tensor([500])}