# Model Card: Mood Machine

## 1. Overview

The Mood Machine is a small text classification project that predicts the mood of a short message. It uses four labels: `positive`, `negative`, `neutral`, and `mixed`.

I built two versions of the system:

- a rule-based model in `mood_analyzer.py`
- a simple ML model in `ml_experiments.py`

The goal of this project was to see how mood prediction changes when I adjust the data, the word lists, and the rules.

## 2. Intended Use

This project is mainly for learning. It works best on short, casual text like student messages, social media-style posts, or quick chat sentences.

It is not meant for serious real-world use. I would not use it for mental health decisions, school discipline, hiring, or anything else where a wrong label could affect someone in an important way.

## 3. Dataset and Labeling

The dataset is stored in `dataset.py`. It currently has 19 labeled posts.

I labeled each post by reading it and deciding whether the overall tone felt positive, negative, neutral, or mixed. Some examples were straightforward:

- `"I love this class so much"` -> `positive`
- `"Today was a terrible day"` -> `negative`

Some were more subjective:

- `"I don't hate it but I don't love it either"` -> `mixed`
- `"today was okay I guess 🥲"` -> `mixed`
- `"This is fine"` -> `neutral`

I tried to make the dataset feel realistic by including:

- slang like `"lowkey"` and `"no cap"`
- emoji like `"😂"`, `"🎉"`, `"😍"`, `"💀"`, and `"🥲"`
- the emoticon `":("`
- negation like `"I am not happy about this"`
- sarcasm like `"I absolutely love getting stuck in traffic"`
- mixed feelings like `"Feeling tired but kind of hopeful"`

The dataset is still very small, so it is useful for learning, but not enough to say the model would work well in the real world.

## 4. How the Rule-Based Model Works

The rule-based model uses a simple set of steps:

1. It preprocesses the text by lowercasing it, removing basic punctuation, and splitting it into tokens.
2. It keeps apostrophes inside words like `"don't"`.
3. It preserves the sad emoticon `":("` so it does not get lost during preprocessing.
4. It splits combined emoji like `"😂🎉"` into separate tokens.
5. It checks each token against `POSITIVE_WORDS` and `NEGATIVE_WORDS` from `dataset.py`.
6. It uses a simple negation rule. If a word like `not` or `don't` comes right before a sentiment word, the meaning gets flipped.
7. It returns:
   - `positive` if it finds only positive signals
   - `negative` if it finds only negative signals
   - `mixed` if it finds both positive and negative signals
   - `neutral` if it finds no sentiment signals

I like this model because it is easy to follow and easy to explain. If it makes a mistake, I can usually see exactly which words or symbols caused it.

## 5. Evaluation Results

I evaluated the rule-based model on the 19 labeled posts in `dataset.py`.

Final rule-based accuracy:

- `0.89`
- `17 out of 19` correct

Some examples it gets right:

- `"Feeling tired but kind of hopeful"` -> `mixed`
- `"I am not sad at all, life is good"` -> `positive`
- `"just got an A on my exam 😂🎉"` -> `positive`
- `"I'm so done with everything 💀"` -> `negative`
- `"nothing is going right :("` -> `negative`

These results improved after I expanded the word lists, improved preprocessing, added emoji handling, and supported the `mixed` label.

The two examples it still gets wrong are:

- `"I absolutely love getting stuck in traffic"` -> predicted `positive`, true `negative`
- `"today was okay I guess 🥲"` -> predicted `negative`, true `mixed`

Those two mistakes show that the model still struggles when tone is indirect or hard to read.

## 6. Comparison with ML Model

The ML model uses `CountVectorizer` and `LogisticRegression`.

Current ML accuracy on the same dataset:

- `1.00`
- `19 out of 19` correct

That is higher than the rule-based model, but this result is also misleading. The ML model is trained and tested on the same 19 posts, so it may be memorizing the training examples instead of learning patterns that would work on new text.

A good example is:

- `"I absolutely love getting stuck in traffic"`

The rule-based model predicts `positive` because it sees the word `"love"`.
The ML model predicts `negative`, which matches the label, but that may be because it already saw that exact sentence during training.

Another example is:

- `"today was okay I guess 🥲"`

The rule-based model predicts `negative` because it treats `🥲` as a negative signal.
The ML model predicts `mixed`, which matches the label on this dataset.

So the ML model looks better in accuracy, but the result is probably too optimistic because the evaluation is not on new examples.

## 7. Limitations

My rule-based model still has a few clear limitations.

- It struggles with sarcasm.
  - Example: `"I absolutely love getting stuck in traffic"`
  - The model sees `"love"` and misses the sarcastic meaning.

- It struggles with subtle tone.
  - Example: `"today was okay I guess 🥲"`
  - A person might read that as mixed, but the model leans negative.

- It depends heavily on exact words and symbols.
  - If a useful word or emoji is not in the word list, the model may miss the mood completely.

- The negation rule is simple.
  - It only works when the negation word comes right before the sentiment word.

- The dataset is small.
  - With only 19 posts, both the rule-based model and the ML model are easy to overfit.

Some of these could be improved with better rules, but some are deeper limitations of rule-based sentiment analysis. Tone, context, and sarcasm are especially hard to capture with simple word matching.

## 8. Ethical Considerations

Even though this is a class project, there are still some important ethical issues to think about.

- The dataset is small and limited.
  - It does not represent all ways people speak, joke, or express emotion.

- Slang and tone can vary by community.
  - A phrase that sounds negative in one context may mean something different in another.

- Mood prediction can feel invasive.
  - If this kind of tool were used on private messages without consent, that would be a problem.

- Wrong labels can matter.
  - If a model misreads sadness, sarcasm, or frustration, it can give the wrong picture of how someone feels.

- The model sounds more confident than it really is.
  - It always returns one label, even when the text is unclear.

## 9. What I Learned

This project showed me that small design choices can change model behavior a lot.

The biggest things I learned were:

- better data makes a big difference
- preprocessing matters more than it seems at first
- rule-based models are easy to explain, which is a real strength
- rule-based models also break easily on sarcasm, subtle tone, and context
- high ML accuracy does not always mean the model is truly better

Overall, I learned that evaluating a model is not just about the final accuracy number. It is about understanding what the model is actually doing, where it fails, and why those failures happen.
