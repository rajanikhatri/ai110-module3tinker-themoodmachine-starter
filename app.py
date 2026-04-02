"""
Simple Streamlit app for the Mood Machine project.
"""

import streamlit as st

from mood_analyzer import MoodAnalyzer


analyzer = MoodAnalyzer()

st.set_page_config(page_title="Mood Machine", page_icon="🙂")

st.title("The Mood Machine")
st.write(
    "Type a short sentence and the rule-based Mood Machine will predict "
    "whether it sounds positive, negative, neutral, or mixed."
)

user_text = st.text_input(
    "Enter a sentence",
    placeholder="Example: I am tired but kind of hopeful",
)

if st.button("Analyze Mood"):
    if not user_text.strip():
        st.warning("Please enter a sentence before analyzing.")
    else:
        prediction = analyzer.predict_label(user_text)
        tokens = analyzer.preprocess(user_text)

        st.subheader("Prediction")
        st.success(f"Predicted mood: {prediction}")

        st.subheader("Preprocessed Tokens")
        st.write(tokens)
