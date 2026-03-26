import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

MODEL_FILE = 'farm_model.pkl'

def train_and_save_model(data):
    X = data[['Avg_Temp', 'Rainfall_mm']]
    y = data['Yield_Qty']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_FILE)

    accuracy = model.score(X_test, y_test)
    return accuracy

def make_prediction(temp, rain):
    if os.path.exists(MODEL_FILE):
        model = joblib.load(MODEL_FILE)
        prediction = model.predict([[temp, rain]])
        return prediction[0]
    else:
        return None
    
def get_feature_importance():
    try:
        model = joblib.load(MODEL_FILE)
        importances = model.feature_importances_
        return importances
    except:
        return None
