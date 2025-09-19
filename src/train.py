# src/train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_model():
    """Trains a Random Forest model and saves it."""
    
    # Define the project directories
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'Crop_recommendation.csv')
    model_path = os.path.join(base_dir, 'models', 'crop_recommender.pkl')

    print("Starting model training...")
    
    # 1. Load the dataset
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        print(f"Error: The file {data_path} was not found. Please ensure it is in the data folder.")
        return

    # 2. Separate features (X) and target (y)
    features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    X = df[features]
    y = df['label']

    # 3. Train the model
    # A Random Forest is great for classification and handles non-linear data well.
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    # 4. Save the trained model
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print("Model trained and saved successfully!")

if __name__ == "__main__":
    train_model()