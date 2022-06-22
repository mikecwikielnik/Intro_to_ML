"""
nltk scrap

https://www.youtube.com/watch?v=WYge0KZBhe0
"""

import nltk
from pyparsing import Word
nltk.download()

text = """Monticello wasn't designated as UNESCO World Heritage Site until 1987 """

import re

re.split("[\s\.\,]", text)

nltk.word_tokenize(text)    # This will split 'wasn't' into 'was', 'n't'

# Stemming 

# There are multiple stemmers in nltk

# Porter stemmer

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

plurals = ['caresses', 'flies', 'dies', 'mules', 'denied', 'died',
           'agreed', 'owned', 'humbled', 'sized', 'meeting', 'stating', 
           'siezing', 'itemization', 'sensational', 'traditional', 'reference',
           'colonizer', 'plotted']

for word in plurals:
    print(f"{word} >>> {stemmer.stem(word)}")
    
# Snowbal stemmer

from nltk.stem.snowball import SnowballStemmer

SnowballStemmer.languages

sn_stemmer = SnowballStemmer("english")

sn_stemmer.stem("generously")

stemmer.stem("generously")

# Lemmatization

# getting the root word

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

for word in plurals:
    print(f"{word} >>> {lemmatizer.lemmatize(word)}")
    
    
    
