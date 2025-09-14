from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd 

# Import the ML model 
with open('Model_3.pkl','rb') as f:
    model = pickle.load(f)

# Pydantic model to validate incoming Data
# R&D Spend	Administration	Marketing Spend	State

class InputData(BaseModel):
    Id: int
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ML Model API is running!"}

@app.post('/predict')
def predict(data: InputData):

    features = [[
        data.Id,
        data.SepalLengthCm,
        data.SepalWidthCm,
        data.PetalLengthCm,
        data.PetalWidthCm
    ]]

    Prediction = model.predict(features)[0]

    return JSONResponse(status_code=200, content={'Predicted_category': Prediction})
