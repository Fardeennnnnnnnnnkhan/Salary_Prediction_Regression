# 💰 Salary Prediction Using Machine Learning (Regression)

An end-to-end **Machine Learning regression project** that predicts an employee's **estimated salary** based on multiple input features.  
The trained model is deployed as an interactive **Streamlit web application** for real-time predictions.

---

## 🚀 Project Overview

Salary prediction is a common regression problem used in HR analytics and business intelligence.  
This project uses supervised machine learning to **predict salary values** based on demographic and professional attributes.

Unlike classification problems, this model predicts a **continuous numerical value**, making it a true **regression task**.

---

## 🎯 Objectives

- Build a regression model to predict salary
- Perform proper data preprocessing and feature scaling
- Train and evaluate the regression model
- Deploy the model using Streamlit
- Provide a clean and interactive UI for users

---

## 🧠 Machine Learning Details

- **Problem Type**: Regression
- **Model Type**: Machine Learning Regression Model
- **Output**: Predicted Salary (numeric value)

---

## 🗂️ Dataset Features

The model uses the following input features:

| Feature | Description |
|------|------------|
| CreditScore | Credit score |
| Gender | Gender of the individual |
| Age | Age |
| Tenure | Years of experience / tenure |
| Balance | Account balance |
| NumOfProducts | Number of products |
| HasCrCard | Credit card ownership |
| IsActiveMember | Active status |
| Geography | Country / region |

> Note: Identifier columns were removed to prevent data leakage.

---

## ⚙️ Tech Stack

- **Programming Language**: Python
- **Libraries Used**:
  - NumPy
  - Pandas
  - Scikit-learn
  - Streamlit
- **Model Persistence**: Pickle (`.pkl`)
- **Version Control**: Git & GitHub

---

## 🔧 Data Preprocessing

- Label Encoding for binary categorical variables
- One-Hot Encoding for multi-class categorical features
- Feature Scaling using `StandardScaler`
- Train-test split for model evaluation

---

## 📊 Model Output

Example output:
```
Predicted Salary: ₹52,340.75
```

This numerical output makes the model useful for:
- HR decision support
- Salary benchmarking
- Business analytics

---

## 🌐 Deployed Streamlit Application

🔗 **Live App Link**  
👉 (https://salarypredictionregression-by-fardeen.streamlit.app/)

*(Replace this link with your actual deployed Streamlit URL)*

---

## ▶️ Run the App Locally

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Salary_Regression_Project/
│
├── app.py                    # Streamlit app
├── model.pkl                 # Trained regression model
├── scaler.pkl                # Feature scaler
├── encoders.pkl              # Encoders
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
└── notebooks/                # Training notebooks
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/Salary-Prediction-Regression.git
cd Salary-Prediction-Regression
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app
```bash
streamlit run app.py
```

---

## ✅ Key Learnings

- Understanding regression problems
- Feature preprocessing for numerical prediction
- Model evaluation for regression tasks
- Deployment of ML models using Streamlit
- End-to-end ML pipeline development

---

## 🎤 Interview-Ready Explanation

> “I built a salary prediction system using a regression model that predicts continuous salary values based on multiple features. The project includes preprocessing, model training, and deployment using Streamlit.”

---

## 🔮 Future Enhancements

- Try advanced regression models
- Add model evaluation metrics (MAE, RMSE, R²)
- Hyperparameter tuning
- Cloud deployment
- Dockerization

---

## 👨‍💻 Author

**Fardeen Khan**  
GitHub: https://github.com/Fardeennnnnnnnnnkhan  

---

⭐ If you found this project useful, consider starring the repository!
