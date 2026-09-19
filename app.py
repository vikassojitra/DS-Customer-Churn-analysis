from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Import the custom transformer so joblib recognizes it during loading
from feature_transformers import FeatureEngineer 

app = Flask(__name__)

# Load the unified model (handles FeatureEngineer -> Preprocessor -> Classifier)
churn_model = joblib.load('model/churn_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Parse incoming JSON request
        data = request.json
        df_input = pd.DataFrame([data])
        
        # 2. Predict directly using the unified pipeline
        prediction = churn_model.predict(df_input)[0]
        probability = churn_model.predict_proba(df_input)[0][1]
        
        # 3. Return the formatted JSON response
        return jsonify({
            "prediction": "Yes" if prediction == 1 else "No",
            "churn_probability": round(float(probability), 2)
        })
        
    except Exception as e:
        # Handle invalid inputs or missing features appropriately
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)