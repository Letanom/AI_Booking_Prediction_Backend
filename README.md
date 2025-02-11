﻿# AI_Booking_Prediction_Backend

This is the backend of the AI Booking Prediction system, which uses machine learning models to predict the likelihood of a user booking a vacation based on their profile information. This repository contains all the necessary components to run the backend server that processes predictions.

## Features
- Train AI models to predict booking status based on user data.
- Endpoint for prediction via POST request.
- Data generation for training.

- ## Requirements

To get started with the backend, you need to install the following dependencies:

1. Python 3.x (recommended version 3.8+)
2. Libraries for the backend application (listed below).

Install the required libraries using the following commands:

### Using `pip`:

- Clone the repository:
  ```bash
  git clone https://github.com/Letanom/AI_Booking_Prediction_Backend.git
  cd AI_Booking_Prediction_Backend

  python -m venv venv
source venv/bin/activate  # I use Windows  `venv\Scripts\activate`


pip install -r requirements.txt
flask
fastapi
pydantic
sklearn
pandas
numpy
joblib


### 4. File Structure

```markdown
## File Structure

The backend project includes the following important files:
- `app.py`: The main API file that runs the FastAPI app and serves the prediction endpoint.
- `data_generator.py`: The script to generate sample data for training the model.
- `train_model.py`: Script to train the model using the sample data.
- `model.pkl`: Saved machine learning model file used for predictions.
- `data.json`: JSON file with user data to train the model.



## Setup and Usage

1. **Train the model**:

   If you want to retrain the AI model, use the `train_model.py` script to train using `data.json`.

   ```bash
   python train_model.py

##Envoirment
python -m uvicorn app:app --reload




### 6. Deployment

```markdown
## Deployment

To deploy this backend on a server, follow these steps:

1. Set up a cloud-based VM (AWS EC2, Google Cloud, etc.).
2. Install dependencies and upload the files.
3. Run `uvicorn` on the server with proper configurations.


Built by me. For learning and increasing my tech skills. I built this app for myself according to my own wishes. Maybe it wouldnt work by to your expectations.
