import re
import pickle

import numpy as np
import streamlit as st
from keras.models import load_model
from tensorflow.keras.utils import pad_sequences

st.image("banner.png", use_container_width=True)

MAX_LEN = 150
LABELS = {0: "Negative", 1: "Neutral", 2: "Positive"}


model = load_model("sentiment_classifier.keras")

with open("stopwords.pkl", "rb") as f:
    stop_words = pickle.load(f)

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)


st.title("Product Reviews Sentiment Analysis")

st.caption("Enter or paste the product review for sentiment prediction")

user_input = st.text_area("Enter product review in text format", height=150)


def preprocess(text):
    text = text.lower()
    clean = re.sub("[^a-z\\s]", "", text)
    cleaned_tok = clean.split()
    tokens = [w for w in cleaned_tok if w not in stop_words]
    return tokens


if st.button("Predict"):
    if not user_input.strip():
        st.warning("Enter the Product Review")
    else:
        tokens = preprocess(user_input)

        if len(tokens) < 2:
            st.warning(
                f"After preprocess we got only {len(tokens)} important words. "
                "To get accurate prediction enter a longer review."
            )
        else:
            seq = tokenizer.texts_to_sequences([tokens])
            pad = pad_sequences(seq, maxlen=MAX_LEN, padding="pre", truncating="post")

            with st.spinner("Analyzing..."):
                probs = model.predict(pad)[0]

            pred = int(np.argmax(probs))
            label = LABELS[pred]
            confidence = probs[pred]

            col1, col2 = st.columns(2)

            with col1:
                st.write("Prediction")
                st.markdown(f"## {label}")

            with col2:
                st.write("Confidence Score")
                st.markdown(f"## {confidence:.2f}")