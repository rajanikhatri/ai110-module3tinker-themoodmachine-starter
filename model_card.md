# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

## 1. Model Overview

**Model type:**
I used both the rule based model and the ML model and compared them.

**Intended purpose:**
Classify short text messages (like social media posts or chat messages) into one of four mood labels: `positive`, `negative`, `neutral`, or `mixed`.

**How it works (brief):**
- **Rule-based:** Each word in the text is checked against a hand-crafted list of positive and negative words. Positive words add +1 to a score, negative words subtract 1. A negation rule (e.g., "not happy") flips the effect of the next word. The final score maps to a label: positive (>0), negative (<0), neutral (=0).
- **ML model:** The texts are converted into word-count vectors using `CountVectorizer` (bag of words), and then a `LogisticRegression` model is trained to predict labels from those vectors.

---

## 2. Data

**Dataset description:**
The dataset starts with 6 labeled example posts in `SAMPLE_POSTS`. I added 8 more for a total of 14 posts. Labels include `positive`, `negative`, `neutral`, and `mixed`.

**Labeling process:**
Labels were assigned by reading each post and judging the overall emotional tone. Some posts were difficult to label — for example, "I don't hate it but I don't love it either" could reasonably be called `neutral` or `mixed`. I chose `mixed` because it expresses both a softened negative and a softened positive at the same time.

**Important characteristics of your dataset:**
- Contains slang: "Lowkey", "no cap"
- Contains sarcasm: "I absolutely love getting stuck in traffic"
- Includes mixed feelings: "tired but kind of hopeful"
- Contains emojis: ":)"
- Contains negation: "I am not sad at all", "I don't hate it"
- Some posts are short and ambiguous: "This is fine", "meh, just another day"

**Possible issues with the dataset:**
- The dataset is very small (14 examples), which makes it easy to overfit.
- Labels for ambiguous posts (sarcasm, mixed feelings) could be debated.
- There is no separate test set — we evaluate on the same data we designed the system around.
- The dataset skews toward English and does not include other languages or dialects.

---

## 3. How the Rule Based Model Works

**Your scoring rules:**
- Each token is checked against a set of positive and negative words.
- If the previous token is a negation word (`not`, `never`, `don't`, `doesn't`, `didn't`, `no`), the score effect is flipped — so "not happy" reduces the score instead of increasing it.
- Final score: `> 0` → `positive`, `< 0` → `negative`, `= 0` → `neutral`.

**Strengths of this approach:**
- Fully transparent — you can trace exactly why a score was assigned to any sentence.
- Handles simple negation correctly (e.g., "I am not happy" → negative).
- Fast and requires no training data or installation of ML libraries.

**Weaknesses of this approach:**
- Cannot detect sarcasm (e.g., "I absolutely love getting stuck in traffic" → predicted `positive`).
- Only knows words that are explicitly in the word list — misses "blessed", "grateful", "worst", "best".
- Cannot produce a `mixed` label — it must pick positive, negative, or neutral.
- Slang like "no cap" or "lowkey" is completely invisible to the model.

---

## 4. How the ML Model Works

**Features used:**
Bag of words using `CountVectorizer` — each unique word in the training data becomes a feature column, and the value is how many times that word appears in the text.

**Training data:**
The model trained on `SAMPLE_POSTS` and `TRUE_LABELS` from `dataset.py` (14 examples total).

**Training behavior:**
Adding more labeled examples improved label coverage — for instance, adding `mixed` examples gave the model a chance to learn that label. With only 14 examples the model likely memorizes the training data, so training accuracy looks very high but real-world performance would be much weaker.

**Strengths and weaknesses:**
- Strength: learns patterns automatically without hand-crafted rules; can learn words the rule-based model misses.
- Weakness: heavily overfits with only 14 examples. Any sentence that looks different from the training data will likely be misclassified.

---

## 5. Evaluation

**How you evaluated the model:**
Both models were evaluated on the 14 labeled posts in `dataset.py`. This is training accuracy only — there is no separate held-out test set.

**Rule-based accuracy observed:** 0.50 (7 out of 14 correct)

**Examples of correct predictions:**
- `"I love this class so much"` → `positive` — "love" is in the positive word list.
- `"Today was a terrible day"` → `negative` — "terrible" is in the negative word list.
- `"I am not sad at all, life is good"` → `positive` — negation flipped "sad", and "good" added +1.

**Examples of incorrect predictions:**
- `"I absolutely love getting stuck in traffic"` → predicted `positive`, true `negative` — sarcasm is invisible; the model only sees the word "love".
- `"feeling so blessed and grateful today :)"` → predicted `neutral`, true `positive` — "blessed" and "grateful" are not in the word list.
- `"this is the worst thing that has ever happened"` → predicted `neutral`, true `negative` — "worst" is not in the word list.

---

## 6. Limitations

- **Tiny dataset:** 14 examples is far too small to build a reliable model.
- **No sarcasm detection:** The rule-based model has no way to understand irony or humor.
- **Limited vocabulary:** The word lists only cover obvious emotional words; everyday words like "blessed", "worst", "best" are missing.
- **No mixed label from rule-based model:** The scoring system cannot output `mixed` — it must always pick one side.
- **Training = test set:** Both models are evaluated on the same data they were built from, which gives an overly optimistic view of performance.

---

## 7. Ethical Considerations

- **Misclassifying distress:** A message like "I'm not doing great" could be predicted as `positive` due to negation + "great". This could cause real harm if the model is used in a mental health or crisis detection context.
- **Slang and dialect bias:** The word lists and training data do not cover African American Vernacular English (AAVE) or other dialects. Phrases like "this is fire" or "I'm dead" will likely be misclassified.
- **Privacy:** Analyzing personal messages for mood without user consent raises serious privacy concerns.
- **Overconfidence:** Both models always output a label even when the text is ambiguous — there is no "I don't know" option, which can make the output seem more reliable than it is.

---

## 8. Ideas for Improvement

- Add significantly more labeled data (hundreds of examples minimum).
- Use TF-IDF instead of raw word counts to reduce the influence of very common words.
- Expand the positive and negative word lists with words like "blessed", "worst", "best", "grateful".
- Add emoji mappings (":)" → positive, "💀" → sarcastic/negative).
- Add a sarcasm detection heuristic (e.g., detecting "I absolutely love [negative situation]").
- Add a real held-out test set to get honest accuracy estimates.
- Use a small pre-trained model (e.g., DistilBERT) for much better language understanding.
