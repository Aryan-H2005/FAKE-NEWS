import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords

# Load model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Text preprocessing
def preprocess(text):

    text = str(text)
    text = text.lower()
    text = re.sub('[^a-zA-Z]', ' ', text)

    words = text.split()

    words = [word for word in words if word not in stop_words]

    return " ".join(words)


# UI
st.title("📰 Fake News Detection System")

st.write("Enter a news article below to check if it is Fake or Real.")

news_input = st.text_area("Enter News Text")

if st.button("Check News"):

    if news_input.strip() == "":
        st.warning("Please enter news text")

    else:

        processed_text = preprocess(news_input)

        vector = vectorizer.transform([processed_text])

        prediction = model.predict(vector)

        if prediction[0] == 1:
            st.error("🚨 Fake News Detected")
        else:
            st.success("✅ Real News")