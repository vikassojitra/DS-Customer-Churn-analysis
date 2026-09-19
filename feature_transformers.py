import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class FeatureEngineer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self # Nothing to fit

    def transform(self, X):
        X_new = X.copy()
        
        # Define services
        service_cols = ['PhoneService', 'MultipleLines', 'OnlineSecurity', 
                        'OnlineBackup', 'DeviceProtection', 'TechSupport', 
                        'StreamingTV', 'StreamingMovies']
        
        # Feature 1: Number of services consumed
        X_new['TotalServices'] = (X_new[service_cols] == 'Yes').sum(axis=1)
        
        # Feature 2: IsAutoPay enabled
        X_new['IsAutoPay'] = X_new['PaymentMethod'].str.contains('automatic', na=False).astype(int)
        
        # Feature 3: Tenure groups
        bins = [0, 12, 24, 36, 48, 60, 100]
        labels = ['0-12', '13-24', '25-36', '37-48', '49-60', '61+']
        X_new['TenureGroup'] = pd.cut(X_new['tenure'], bins=bins, labels=labels, include_lowest=True).astype(str)
        
        # Remove original numerical 'tenure' column
        if 'tenure' in X_new.columns:
            X_new.drop(columns=['tenure'], inplace=True)
            
        return X_new