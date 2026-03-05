from fastapi import FastAPI
import joblib 
from paths import * 
import numpy as np

app = FastAPI()


@app.get("/home")
def home():
    return "Hello project API"

@app.post("/prediction")
def prediction(SeniorCitizen:float,tenure:float,MonthlyCharges:float):
    input_data = np.array([[SeniorCitizen,tenure,MonthlyCharges]])

    model = joblib.load(model_path)
    print("Model loaded...!")

    prediction =  model.predict(input_data)

    prediction = prediction.tolist()
    return prediction

