import numpy
import random
import nltk
import tflearn
import tensorflow as tf
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()
import json

with open("intents.json") as file:
    data = json.load(file)
print(file)


words = []
labels = []
docs = []
for intent in file["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs.append(pattern)
    if intent["tag"] not in labels:
        labels.append(intent["tag"])

print("it worked")
