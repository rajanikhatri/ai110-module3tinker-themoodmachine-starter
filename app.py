"""
Simple Streamlit app for the Mood Machine project.
"""

import streamlit as st

from mood_analyzer import MoodAnalyzer


analyzer = MoodAnalyzer()

EXAMPLE_SENTENCES = {
    "Sarcasm": "I absolutely love getting stuck in traffic",
    "Mixed Feelings": "Feeling tired but kind of hopeful",
    "Super Positive": "just got an A on my exam 😂🎉",
}


def load_example(example_text: str) -> None:
    """Load an example sentence into the input box."""
    st.session_state.user_text = example_text
    st.session_state.prediction = None
    st.session_state.tokens = []


if "user_text" not in st.session_state:
    st.session_state.user_text = ""

if "prediction" not in st.session_state:
    st.session_state.prediction = None

if "tokens" not in st.session_state:
    st.session_state.tokens = []


st.set_page_config(page_title="Mood Machine", page_icon="🙂")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f4f2ff 0%, #fff7fb 55%, #f3f5ff 100%);
    }

    .block-container {
        max-width: 860px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    .mood-header {
        text-align: center;
        margin-bottom: 2rem;
    }

    .mood-title {
        font-size: 3.2rem;
        font-weight: 700;
        line-height: 1.1;
        color: #5a3fd7;
        margin-bottom: 0.75rem;
    }

    .mood-subtitle {
        font-size: 1.1rem;
        color: #4b5563;
        margin: 0 auto;
        max-width: 700px;
    }

    .examples-label {
        text-align: center;
        font-size: 0.95rem;
        font-weight: 600;
        color: #7c3aed;
        margin: 1.5rem 0 0.75rem 0;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, 0.94);
        border: 1px solid rgba(255, 255, 255, 0.75);
        border-radius: 24px;
        padding: 1.4rem;
        box-shadow: 0 18px 45px rgba(93, 74, 155, 0.12);
    }

    div[data-testid="stTextArea"] textarea {
        border-radius: 16px;
        min-height: 140px;
    }

    div.stButton > button {
        border-radius: 999px;
        min-height: 3rem;
        font-weight: 600;
    }

    div.stButton > button[kind="primary"] {
        background: linear-gradient(90deg, #8b5cf6 0%, #ec4899 100%);
        color: white;
        border: none;
        font-size: 1rem;
        padding: 0.4rem 1.25rem;
        box-shadow: 0 12px 22px rgba(139, 92, 246, 0.22);
    }

    div.stButton > button[kind="primary"]:hover {
        filter: brightness(1.04);
    }

    .prediction-section {
        margin-top: 2.25rem;
    }

    .tokens-label {
        margin-top: 1rem;
        font-weight: 600;
        color: #374151;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="mood-header">
        <div class="mood-title">The Mood Machine</div>
        <div class="mood-subtitle">
            Enter a sentence and the rule-based Mood Machine will predict
            whether it sounds positive, negative, neutral, or mixed.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="examples-label">Try these examples</div>', unsafe_allow_html=True)

example_col_1, example_col_2, example_col_3 = st.columns(3)

with example_col_1:
    st.button(
        "Sarcasm",
        use_container_width=True,
        on_click=load_example,
        args=(EXAMPLE_SENTENCES["Sarcasm"],),
    )

with example_col_2:
    st.button(
        "Mixed Feelings",
        use_container_width=True,
        on_click=load_example,
        args=(EXAMPLE_SENTENCES["Mixed Feelings"],),
    )

with example_col_3:
    st.button(
        "Super Positive",
        use_container_width=True,
        on_click=load_example,
        args=(EXAMPLE_SENTENCES["Super Positive"],),
    )

st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

input_card = st.container(border=True)

with input_card:
    user_text = st.text_area(
        "Type a sentence",
        key="user_text",
        placeholder="Type your sentence here and click Analyze Mood.",
        height=140,
    )

    st.markdown("<div style='height: 0.75rem;'></div>", unsafe_allow_html=True)

    button_left, button_center, button_right = st.columns([1, 1.4, 1])
    with button_center:
        analyze_clicked = st.button(
            "Analyze Mood",
            use_container_width=True,
            type="primary",
        )

if analyze_clicked:
    if not user_text.strip():
        st.session_state.prediction = None
        st.session_state.tokens = []
        st.warning("Please enter a sentence before analyzing.")
    else:
        st.session_state.prediction = analyzer.predict_label(user_text)
        st.session_state.tokens = analyzer.preprocess(user_text)

st.markdown('<div class="prediction-section"></div>', unsafe_allow_html=True)
st.subheader("Prediction")

prediction = st.session_state.prediction
tokens = st.session_state.tokens

if prediction is None:
    st.info("Enter a sentence and click Analyze Mood to see the result.")
else:
    message = f"Predicted mood: {prediction}"

    if prediction == "positive":
        st.success(message)
    elif prediction == "negative":
        st.error(message)
    elif prediction == "neutral":
        st.info(message)
    elif prediction == "mixed":
        st.warning(message)

    st.caption(
        "This result is based on a rule-based model using keywords and "
        "emoji signals."
    )

    st.markdown('<div class="tokens-label">Tokens used during preprocessing:</div>', unsafe_allow_html=True)
    st.write(tokens)
