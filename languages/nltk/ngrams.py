"""
ngrams
"""

from nltk import ngrams

RESUME = 'London Ho Chi Minh City'
N = 4
bigrams = ngrams(RESUME.split(), N)

for grams in bigrams:
    print(type(grams), grams)
