from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# CORS config
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

# User data class
class UserData(BaseModel):
    Age: int
    Income: float  
    FamilySize: int
    HotelStar: int
    TravelFrequency: int
    PreviousBookings: int
    VacationSpendLastYear: float
    ChildrenCount: int
    StayDuration: int

# Load the model
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    raise HTTPException(
        status_code=500, detail="Model file 'model.pkl' not found. Please ensure it exists."
    )


def predict_booking(data: UserData):

  
    # Convert the input data to a pandas DataFrame
    input_data = pd.DataFrame([data.dict()])

    # Make a prediction
    try:
        prediction = model.predict(input_data)[0]

        # Convert numpy types to Python native types for JSON serialization
        if isinstance(prediction, np.integer):  # Check for numpy int
            prediction = int(prediction)
        elif isinstance(prediction, np.float64):  # Check for numpy float
            prediction = float(prediction)

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error making prediction: {str(e)}"
        )

    # Return the prediction
    return {"BookingStatus": prediction}

#API endpoint
@app.post("/predict")
def predict(data: UserData):
  
    return predict_booking(data)

# Test the API
@app.get("/")
def read_root():
    return {"message": "Booking prediction API is running!"}
