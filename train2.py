# Import the libraries
import json
import numpy
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from tokenizationAndStemming import tokenize, stem, BagOfWords

from model import NeuralNet


# 2> create collection according to input


def createCollection(fName, which, name):
    allWords = []
    tags = []
    collection = []
    key = 'intents' if which == 1 else 'attributes'
    print(key, 55)
    for value in fName[key]:
        tag = value[name]
        tags.append(tag)
        for pattern in value['patterns']:
            words = tokenize(pattern)
            allWords.extend(words)
            collection.append((words, tag))
    ignoreWords = ['?', ';', ',', '.', '!']
    allWords = [stem(w) for w in allWords if w not in ignoreWords]
    allWords = sorted(set(allWords))
    tags = sorted(set(tags))

    return collection, allWords, tags


# main operating area of training
def main():
    # 1>open the appropriate files
    # Open the intents.json file in read mode
    with open('intents.json', 'r') as f:
        intents = json.load(f)
    # open the attribute file as attribute
    with open('attributes.json', 'r') as p:
        attributes = json.load(p)

    collection1, allWords1, tags1 = createCollection(intents, 1, "tags")
    collection2, allWords2, tags2 = createCollection(attributes, 2, "attr")

    print(collection2)


if __name__ == "__main__":
    main()
