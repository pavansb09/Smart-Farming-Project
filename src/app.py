# src/app.py
import joblib
import os
import numpy as np
from flask import Flask, render_template, request, url_for

# Define the project directories
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(base_dir, 'models', 'crop_recommender.pkl')
template_path = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_path)

# Load the pre-trained model
try:
    model = joblib.load(model_path)
    print("Model loaded successfully.")
except FileNotFoundError:
    model = None
    print("Error: Model file not found. Please run src/train.py first.")

@app.route('/')
def home():
    """Renders the main HTML page."""
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    """Handles the recommendation request."""
    if not model:
        return "Error: Model not loaded. Please train the model first.", 500

    try:
        # Get data from the form
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Create a NumPy array for prediction (recommendation)
        features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        
        # Make the recommendation
        recommendation = model.predict(features)[0]
        
        # Return the result to the HTML page
        return render_template('index.html', recommendation_text=f'The recommended crop is: {recommendation.title()}')

    except ValueError:
        return "Invalid input. Please enter valid numbers.", 400

if __name__ == '__main__':
    # Flask will automatically handle redirects for '/' and '/recommend'
    app.run(debug=True)