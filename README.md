## AI-Based Heart Disease Risk Prediction System

### Project Overview
This project is an end-to-end Machine Learning application that predicts the risk of heart disease based on patient health parameters. It uses supervised learning models and is deployed using Streamlit for real-time predictions.

The goal is to assist in early detection and risk assessment using data-driven methods.

---

### Features
- Exploratory Data Analysis (EDA)
- Data Preprocessing & Feature Scaling
- Machine Learning Models:
  - Logistic Regression
  - Random Forest Classifier
- Model Evaluation (Accuracy, ROC Curve)
- Web App Deployment using Streamlit
- Real-time Prediction System

---

### Dataset
- Source: UCI Heart Disease Dataset
- Records: 900+ Patients
- Features: Age, Sex, BP, Cholesterol, ECG, Heart Rate, etc.

---

###  Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Google Colab
- GitHub

---

### Machine Learning Workflow
1. Data Cleaning & Handling Missing Values  
2. Exploratory Data Analysis  
3. Feature Engineering  
4. Model Training  
5. Model Comparison  
6. Hyperparameter Tuning  
7. Deployment

---

### Model Performance

| Model               | Accuracy | Precision | Recall | F1-Score |
|---------------------|----------|-----------|--------|----------|
| Logistic Regression | 81.52%   | 81.48%    | 86.27% | 83.81%   |
| Random Forest       | 85.33%   | 83.78%    | 91.18% | 87.32%   |

Random Forest was selected for deployment due to better overall performance.


(Random Forest selected for deployment)

---

### Live Demo
Deployed App:  
Streamlit link- https://heartdiseaseprediction-9g4cajiz5lmpuyfntagpfk.streamlit.app/

---

### How to Run Locally

```bash
git clone https://github.com/your-username/heart_disease_prediction.git
cd heart_disease_prediction
pip install -r requirements.txt
streamlit run app.py
