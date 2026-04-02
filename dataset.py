"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    "hopeful",
    "proud",
    "blessed",
    "grateful",
    "best",
    "immaculate",
    "😂",
    "🎉",
    "😍",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    "worst",
    "done",
    "💀",
    "🥲",
    ":(",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
]

# Added more posts with varied language styles, slang, emojis, sarcasm, and negation.
SAMPLE_POSTS.extend([
    "Lowkey stressed but kind of proud of myself",      # mixed
    "I absolutely love getting stuck in traffic",        # sarcasm -> negative
    "no cap this was the best day ever",                 # slang -> positive
    "I don't hate it but I don't love it either",        # mixed
    "feeling so blessed and grateful today :)",          # positive
    "this is the worst thing that has ever happened",    # negative
    "meh, just another day I guess",                     # neutral
    "I am not sad at all, life is good",                 # positive (negation)
    "just got an A on my exam 😂🎉",                    # positive
    "I'm so done with everything 💀",                   # negative (slang: 💀 = exhausted)
    "today was okay I guess 🥲",                        # mixed (smiling through sadness)
    "vibes are immaculate today 😍",                    # positive
    "nothing is going right :(",                        # negative
])

TRUE_LABELS.extend([
    "mixed",
    "negative",
    "positive",
    "mixed",
    "positive",
    "negative",
    "neutral",
    "positive",
    "positive",
    "negative",
    "mixed",
    "positive",
    "negative",
])

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
