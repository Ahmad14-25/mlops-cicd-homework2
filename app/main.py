from fastapi import FastAPI
from app.features import hash_feature
from app.model import predict

app = FastAPI()

@app.get("/predict")
def get_prediction(text: str):
    feature = hash_feature(text)
    result = predict(feature)
    return {"prediction": result}
