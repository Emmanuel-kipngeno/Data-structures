import re
from collections import Counter

def word_frequency(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())
    return dict(Counter(words))


if __name__ == "__main__":
    sentence = "This is a test sentence. This sentence is a test."
    result = word_frequency(sentence)
    print(result)
