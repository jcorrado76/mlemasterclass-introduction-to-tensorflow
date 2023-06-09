from fastapi import FastAPI

import pydantic

import joblib
import numpy as np

from sklearn.datasets import load_iris

app = FastAPI()

iris_class_names = load_iris().target_names
model = joblib.load("model.joblib")

class IrisSample(pydantic.BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def hello_world():
    return {"message": "Hello World!"}


@app.get("/predict")
async def predict(sample: IrisSample):
    prediction = model.predict(np.asarray([[
        sample.sepal_length,
        sample.sepal_width,
        sample.petal_length,
        sample.petal_width
    ]]))
    return {"prediction": iris_class_names[prediction[0]]}
