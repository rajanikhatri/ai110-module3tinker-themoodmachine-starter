# Model Card: Mood Machine

## 1. Overview of the Mood Machine

The Mood Machine is a small text classification project that tries to guess the mood of a short post or message. It uses four labels:

- `positive`
- `negative`
- `neutral`
- `mixed`

This project includes two versions of the model:

- a rule-based model in `mood_analyzer.py`
- a simple machine learning model in `ml_experiments.py`

The goal of the project was not just to get predictions, but to see how model choices, word lists, and labeled data affect behavior.

## 2. Intended Use

This project is meant for learning and experimentation. It is designed for short, casual text like:

- student-style messages
- social posts
- quick chat messages

It is not meant for high-stakes use like mental health screening, school discipline, hiring, or anything serious where a wrong label could harm someone.

## 3. Dataset and Labeling

The dataset lives in `dataset.py`. Right now it has 19 short example posts and 19 matching labels.

The labels were chosen by reading each post and deciding whether the tone felt mostly positive, negative, neutral, or mixed. Some examples were easy to label, like:

- `"I love this class so much"` -> `positive`
- `"Today was a terrible day"` -> `negative`

Some examples were harder and more subjective, like:

- `"I don't hate it but I don't love it either"` -> `mixed`
- `"today was okay I guess 🥲"` -> `mixed`
- `"This is fine"` -> `neutral`

I tried to make the dataset feel realistic by including:

- slang: `"lowkey"`, `"no cap"`
- emojis: `"😂"`, `"🎉"`, `"😍"`, `"💀"`, `"🥲"`
- emoticons: `":("`
- negation: `"I am not happy about this"`
- sarcasm: `"I absolutely love getting stuck in traffic"`
- mixed emotions: `"Feeling tired but kind of hopeful"`

This dataset is still very small, so it is useful for learning, but not enough to build a reliable real-world model.

## 4. How the Rule-Based Model Works

The rule-based model is in `mood_analyzer.py`.

It works in a few simple steps:

1. It preprocesses the text by lowercasing it, removing basic punctuation, keeping apostrophes in words like `"don't"`, and splitting the text into tokens.
2. It preserves some useful emotion signals during preprocessing, like the sad emoticon `":("`.
3. It can also split combined emoji like `"😂🎉"` into separate tokens so each emoji can be checked.
4. It compares each token to hand-written `POSITIVE_WORDS` and `NEGATIVE_WORDS` from `dataset.py`.
5. It uses a simple negation rule. If the previous token is something like `not` or `don't`, it flips the meaning of the next sentiment word.
6. It returns:
   - `positive` if it finds only positive signals
   - `negative` if it finds only negative signals
   - `mixed` if it finds at least one positive and one negative signal
   - `neutral` if it finds no sentiment signals

This makes the model easy to understand because I can trace why it made a decision.

## 5. Evaluation Results

I evaluated the rule-based model on the 19 labeled posts in `dataset.py`.

Current rule-based accuracy:

- `0.89`
- `17 out of 19` correct

Examples it gets right:

- `"Feeling tired but kind of hopeful"` -> `mixed`
- `"I am not sad at all, life is good"` -> `positive`
- `"just got an A on my exam 😂🎉"` -> `positive`
- `"I'm so done with everything 💀"` -> `negative`
- `"nothing is going right :("` -> `negative`

Main observations:

- The model improved a lot after I expanded the word lists.
- Adding support for `mixed` helped with examples that had both positive and negative signals.
- Improving preprocessing also helped because emoji and `:(` were being lost before.

The two examples it still gets wrong are:

- `"I absolutely love getting stuck in traffic"` -> predicted `positive`, true `negative`
- `"today was okay I guess 🥲"` -> predicted `negative`, true `mixed`

These mistakes show that the model still struggles with sarcasm and subtle tone.

## 6. Comparison With the ML Model

The ML model in `ml_experiments.py` uses `CountVectorizer` and `LogisticRegression`.

Current ML accuracy on the same 19 posts:

- `1.00`
- `19 out of 19` correct

At first, this looks better than the rule-based model. But there is an important catch: the ML model is trained and tested on the same small dataset.

So the ML model may be doing so well because it has basically learned the exact examples it already saw.

A good example is:

- `"I absolutely love getting stuck in traffic"`

The rule-based model predicts `positive` because it sees the word `"love"`.
The ML model predicts `negative`, probably because that exact labeled example was part of the training data.

Another example is:

- `"today was okay I guess 🥲"`

The rule-based model predicts `negative` because it notices the negative emoji.
The ML model predicts `mixed`, which matches the label better on this dataset.

So the ML model performs better here, but the score is probably too optimistic because the evaluation is not on new data.

## 7. Known Limitations

My current rule-based model still has some clear limitations.

- **Sarcasm is hard to detect.**
  - Example: `"I absolutely love getting stuck in traffic"`
  - The model sees `"love"` and treats it as positive.

- **Subtle tone is hard to capture.**
  - Example: `"today was okay I guess 🥲"`
  - A person might read this as mixed or uncertain, but the model leans negative.

- **The model depends on exact words and symbols.**
  - If I do not put a word or emoji in the word list, the model may miss it completely.

- **The negation rule is simple.**
  - It only checks the word right before a sentiment word, so more complex phrasing can still confuse it.

- **The dataset is tiny.**
  - With only 19 examples, both models are easy to overfit and hard to trust on new text.

Some of these are small rule issues, but some are deeper limits of rule-based sentiment analysis. Tone, context, and sarcasm are especially hard to solve with simple word matching.

## 8. Ethical Considerations and Bias

Even though this is a classroom project, there are still important ethical issues to think about.

- **Bias in language coverage**
  - The dataset is small and mostly written in one casual English style.
  - It does not represent many dialects, communities, or ways of expressing emotion.

- **Slang can be misunderstood**
  - Some slang changes meaning depending on context, friend group, or community.
  - A phrase that sounds negative to the model might not actually be negative to a person.

- **Private messages are sensitive**
  - Mood analysis on personal writing can feel invasive if people do not know it is happening.

- **Wrong labels can matter**
  - A model that misreads sadness, sarcasm, or distress could give the wrong impression about how someone feels.

- **Overconfidence**
  - The model always returns one label, even when the text is vague or hard to interpret.
  - That can make it seem more certain than it really is.

## 9. What I Learned From This Project

This project helped me understand that even a small model involves a lot of design choices.

What I learned most:

- Data matters a lot. Adding better examples and labels changed model behavior quickly.
- Small preprocessing choices matter. Emoji handling and preserving `:(` changed the predictions.
- Rule-based systems are easy to understand, which is a big strength.
- At the same time, rule-based systems miss tone, context, and sarcasm very easily.
- A higher ML accuracy number does not always mean the model is truly better. If the model is tested on the same data it trained on, the result can be misleading.

Overall, the biggest lesson was that building a model is not just about getting a number. It is also about understanding why the model behaves the way it does, where it fails, and what those failures mean.
