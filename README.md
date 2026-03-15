# 📰 Fake News Detection using Machine Learning

## 📌 Project Overview

Fake news spreading through online media and social platforms has become a serious problem.
This project builds a **machine learning model** to classify news articles as **Fake or Real** based on textual content.

The system uses **Natural Language Processing (NLP)** techniques and a machine learning classifier to analyze news articles and detect misinformation.

---

## 🎯 Objective

* Detect whether a news article is **Fake or Real**
* Apply **text preprocessing and feature extraction**
* Train a **machine learning classification model**
* Deploy an interactive **web application**

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Streamlit

---

## 📊 Dataset

The dataset consists of two CSV files:

* **Fake.csv**
* **True.csv**

Columns in the dataset:

* title
* text
* subject
* date

A label column is created during preprocessing:

* **1 → Fake News**
* **0 → Real News**

The dataset is commonly available on Kaggle.

---

## ⚙️ Project Workflow

1. Data Collection
2. Data Cleaning
3. Text Preprocessing
4. Feature Extraction using TF-IDF
5. Train Machine Learning Model
6. Model Evaluation
7. Deployment using Streamlit

---

## 🤖 Machine Learning Model

The model used in this project:

**Logistic Regression**

Steps involved:

* Combine **title + text**
* Apply **text preprocessing**
* Convert text to numerical features using **TF-IDF Vectorizer**
* Train classifier to detect fake news.

---

## 📈 Model Performance

Evaluation metrics used:

* Accuracy
* Precision
* Recall
* F1 Score

The model achieves approximately **95–98% accuracy** on the test dataset.

---

## 💻 Web Application

A simple web interface was developed using **Streamlit** where users can:

1. Enter a news article
2. Click **Check News**
3. Get prediction → **Fake or Real**

---

## 🚀 How to Run the Project

### 1️⃣ Clone Repository

git clone https://github.com/Aryan-H2005/FAKE-NEWS.git

### 2️⃣ Install Dependencies

pip install -r requirements.txt

### 3️⃣ Run the Streamlit App

streamlit run app.py

### 4️⃣ LIVE DEMO
Link : https://fake-news-rswjf7zugt48rncqt6sq8c.streamlit.app/

The application will open in your browser.

---

## 📂 Project Structure

fake-news-detection
│
├── Fake.csv

├── True.csv

├── app.py

├── fake_news_model.pkl

├── vectorizer.pkl

├── requirements.txt

└── README.md

---

## 🔮 Future Improvements

* Use deep learning models such as **LSTM**
* Add **visualization dashboards**
* Improve preprocessing with advanced NLP technique

---

## 👨‍💻 Author

Aryan Harke

Data Science Enthusiast
