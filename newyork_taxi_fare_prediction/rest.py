"""module for API for calling models"""

from typing import Dict
from fastapi import FastAPI
import torch

# Creating an instance of App
app = FastAPI()

# Get model for model calls

@app.get("/")
def get_predictions(model_feature_values: torch.Tensor) -> Dict
