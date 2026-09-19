# Customer Churn Prediction API

This project builds and serves a machine learning model to predict whether a telecom customer is likely to churn.

## Project Overview

The application loads a trained scikit-learn pipeline from `model/churn_model.pkl` and exposes a Flask REST API to make predictions for new customer records.

The custom feature engineering logic is defined in `feature_transformers.py` and is used to create derived features such as:

- Total services used
- Auto-pay flag
- Tenure group

## Tech Stack

- Python
- Flask
- pandas
- scikit-learn
- joblib

## Project Structure

- `app.py` — Flask API entry point
- `feature_transformers.py` — custom preprocessing logic
- `model/churn_model.pkl` — trained churn prediction model
- `data/` — dataset files
- `sample_request.json` — sample JSON payload for testing the API
- `requirements.txt` — Python dependencies
- [Customer_Churn_Final_Business_Analysis.docx](Customer_Churn_Final_Business_Analysis.docx) — business analysis report

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the API

```bash
python app.py
```

The API will run locally at:

```text
http://127.0.0.1:5000
```

## Endpoint

### POST /predict

Send a JSON object with customer details to get churn prediction.

### Example request

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d @sample_request.json
```

### Example response

```json
{
  "prediction": "No",
  "churn_probability": 0.19
}
```

## Notes

- `prediction` returns either `Yes` or `No`.
- `churn_probability` is the probability that the customer will churn.
- The app expects the input fields to match the original training data schema.

## Final Business analysis report

- [Customer_Churn_Final_Business_Analysis.docx](Customer_Churn_Final_Business_Analysis.docx) — Check this file

## Author

- Vikas Sojitra

## Video Demonstration

- **Google Drive Link:**https://drive.google.com/file/d/1YiD59SIZhdCevNZbfSTOrVkeCZRssmQM/view?usp=sharing