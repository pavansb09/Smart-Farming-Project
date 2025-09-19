## 🌾 Smart Farming Crop Yield Prediction
📌 Project Overview

This project is a Smart Farming Application that predicts crop yield based on environmental and soil factors.
It uses Machine Learning (Random Forest) to analyze data like rainfall, temperature, humidity, and soil type, and then predicts the expected yield.

The solution is built for farmers and agricultural planners to optimize decision-making and improve crop productivity.

## 🚀 Features

✅ Predicts crop yield based on soil & weather conditions
✅ Web interface (Flask + HTML) for user-friendly input
✅ Machine Learning model trained on agricultural dataset
✅ Easy to deploy and extend with new data


## 📂 Project Structure

- **data/**
  - `Crop_recommendation.csv` → Dataset  

- **models/**
  - `crop_recommender.pkl` → Saved ML model  

- **src/**
  - `app.py` → Flask application (backend)  
  - `train.py` → Model training script  

- **templates/**
  - `index.html` → Frontend (UI)  

- **requirements.txt** → Project dependencies  
- **README.md** → Project documentation  



## ⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/pavansb09/Smart-Farming-Project.git
cd Smart-Farming-Project

2️⃣ Create virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Train the model
python src/train.py

5️⃣ Run the Flask app
python src/app.py

6️⃣ Open in browser
http://127.0.0.1:5000/

## 📊 Tech Stack

Python (Flask, Pandas, Scikit-learn, Numpy)

Machine Learning (Random Forest Regressor)

HTML + CSS (Frontend)

## 📸 Screenshots

<img width="460" height="640" alt="Screenshot 2025-09-19 141613" src="https://github.com/user-attachments/assets/27e02674-5b4e-479d-bfde-378197793b56" />
<img width="406" height="87" alt="Screenshot 2025-09-19 141630" src="https://github.com/user-attachments/assets/df2c6c1b-4a19-41c4-8ac4-fbe99c163de8" />


## 🎯 Future Enhancements

Add more environmental features (fertilizer, pH value, pest data)

Deploy to Heroku / Render / AWS for public access

Create a mobile app interface for farmers

## 👨‍💻 Author

Pavan SB – Developer & Researcher

GitHub : https://github.com/pavansb09

LinkedIn : https://www.linkedin.com/in/pavansb1


## 📜 License

This project is open-source under the MIT License.
