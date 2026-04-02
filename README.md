# The Mood Machine

## Live Demo

https://ai110-module3tinker-themoodmachine-starter-rgdsvmvncm98piorscw.streamlit.app/

## Overview

The Mood Machine is a rule-based sentiment analysis app that predicts whether a sentence sounds positive, negative, neutral, or mixed. It uses simple text rules to look for mood signals in words, emojis, and emoticons. I improved the project by cleaning the text more carefully, expanding the word lists, improving emoji handling, and adding support for mixed emotions.

## Features

- Rule-based mood prediction
- Handles emojis and emoticons
- Supports mixed emotions
- Interactive Streamlit UI

## How It Works

1. The app preprocesses the text by cleaning it, lowering the case, and keeping useful signals like emojis and emoticons.
2. It scores the sentence using positive and negative word lists, along with simple rules for things like negation.
3. It compares those signals and predicts one of four labels: positive, negative, neutral, or mixed.

## Example Inputs

- "I absolutely love getting stuck in traffic"
- "Feeling tired but kind of hopeful"
- "just got an A on my exam 😂🎉"

## Results

The rule-based model reached an accuracy of 0.89, which means it predicted 17 out of 19 examples correctly on this dataset.

The ML model reached an accuracy of 1.00, but it was trained and tested on the same dataset. That means the score looks perfect, but it is not a reliable measure of how well the model would perform on new examples.

## Limitations

- Sarcasm is hard to detect
- Subtle tone can be misclassified

## Tech Stack

- Python
- Streamlit
- scikit-learn
