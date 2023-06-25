# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 17:37:34 2023

@author: dottd


"""

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))

def remove_stop_words(arr, stop_words):
    arr_temp = []
    for word in arr:
        if word.lower() not in stop_words:  # Convert word to lowercase for case-insensitive comparison
            arr_temp.append(word)
    return arr_temp

def createFile(path, content):
    with open(path, 'w') as file:
        file.write(content)

path = "example.txt"
content = """ancient Rome refers to
in the ancient world, at its height in AD 117"""

createFile(path, content)

print(f"File '{path}' created.")

def readFile(path):
    with open(path, 'r') as file:
        text = file.read()
    return text

text = readFile(path)
print(text)

def splitter(text):
    return text.split()

arr = splitter(text)

arr_temp = remove_stop_words(arr, stop_words)

count = 0

for el in arr_temp:
    print(el)
    count += 1

print("Total words:", count)


import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()
arr_temp = ["word", "wordish", "worded"]
lemmatized_words = [lemmatizer.lemmatize(word) for word in arr_temp]

print(arr_temp)
print(lemmatized_words)

    
    
#Export to Json
def saveFreqToJson(count, pathJson):
    with open(pathJson, 'w') as json_file:
        json.dump(count, json_file)
    
pathJson = "jsonFile.json"

saveFreqToJson(count, pathJson)
    
    
    
    
    
    
    
    
    
    
    