# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:18:45 2023

@author: dottd
"""

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import json

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def split_text(text):
    return nltk.word_tokenize(text)

def remove_stop_words(words, stop_words):
    return [word for word in words if word.lower() not in stop_words]

def lemmatize_words(words_clean):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in words_clean]

def compute_frequency_words(words_lemmatized):
    word_freq = {}
    for word in words_lemmatized:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

def save_words_frequency(words_frequency, file_path="data/words_frequency.json"):
    with open(file_path, 'w') as json_file:
        json.dump(words_frequency, json_file)

stop_words = set(stopwords.words('english'))

text = read_text_file("data/text.txt")
words = split_text(text)
words_clean = remove_stop_words(words, stop_words)
words_lemmatized = lemmatize_words(words_clean)
words_frequency = compute_frequency_words(words_lemmatized)
save_words_frequency(words_frequency, file_path="data/words_frequency.json")
