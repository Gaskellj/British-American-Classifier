"""

Text Classification For Dialog Recognition on English and American Corpora

Author: Colby Beach, James Gaskell, Kevin Welch and Kristina Streignitz

We affirm that we have carried out my academic endeavors with full
academic honesty. Colby Beach, James Gaskell, Kevin Welch

"""


from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

import random
from collections import Counter
import numpy as np

from evaluation import evaluate
import os

# Load data

amerWords = []
my_file = open("spellingList/AmericanSpelling.txt", "r")
data = my_file.read()
amerWords.extend(data.split("\n"))
my_file.close()


britWords = []
my_file = open("spellingList/BritishSpelling.txt", "r")
data = my_file.read()
britWords.extend(data.split("\n"))
my_file.close()

amerSlang = []
my_file = open("slangList/americanSlang.txt", "r")
data = my_file.read()
amerWords.extend(data.split("\n"))
my_file.close()


britSlang = []
my_file = open("slangList/britishSlang.txt", "r")
data = my_file.read()
britWords.extend(data.split("\n"))
my_file.close()


def create_training_and_dev_sets():


    #looping through American data files
    amerSent = []
    directory = os.fsencode("sentenceTrain/America")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        my_file = open("sentenceTrain/America/" + filename, "r")
        data = my_file.read()
        amerSent.extend(data.split("\n"))
        my_file.close()


    #looping through British data files
    britSent = []
    directory = os.fsencode("sentenceTrain/British")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        my_file = open("sentenceTrain/British/" + filename, "r")
        data = my_file.read()
        britSent.extend(data.split("\n"))
        my_file.close()


    labels = [1 for sent in amerSent]
    labels += [0 for sent in britSent]


    sentences = []
    sentences.extend(amerSent)
    sentences.extend(britSent)


    # Split into training set and development set
    dev_selection = random.sample(range(0, len(sentences)), 500)
    dev_reviews = [input("Enter a sentence:")]
    print("Predicting...")

    training_reviews = [sentences[i] for i in range(len(sentences)) if i not in dev_selection]

    training_word_counts = Counter([w.lower() for review in training_reviews for w in review])
    vocab = [word_count[0] for word_count in training_word_counts.most_common(2000)]

    training_x = np.array([create_features(r, vocab) for r in training_reviews])
    dev_x = np.array([create_features(r, vocab) for r in dev_reviews])

    training_y = np.array([labels[i] for i in range(len(labels)) if i not in dev_selection])

    return training_x, training_y, dev_x


def create_features(sentence, vocab):
    features = [] 

    #Given feature
    word_counts = Counter(sentence)
    features.extend([int(word_counts[w] > 0) for w in vocab])
    
    #If a british or american spelling or slang appears in the sentence
    features.extend(checkSpellings(sentence))
    features.extend(checkSlang(sentence))
    features.extend(finalThree(sentence))

    return features


def checkSlang(sentence):
    british = 0
    american = 0
    for word in sentence.split():
        if word.title() in amerSlang:
            american += 1
        elif word.title() in britSlang:
            british += 1
    
    return [british, american]

def checkSpellings(sentence):
    
    british = 0
    american = 0

    for word in sentence.split():
        if word.lower() in amerWords:
            american += 1
        elif word.lower() in britWords:
            british += 1
    
    return [british, american]

def finalThree(sentence):
    british = 0
    american = 0
    for word in sentence.split():
        finalthree = word[-3:]
        if finalthree == 'our':
            british += 1
        elif finalthree == 'ise':
            british += 1
        elif finalthree == 'ize':
            american += 1
        elif word[-2:] == 'or':
            american += 1

    return [british, american]

if __name__ == "__main__":
    # Create training and development/test set
    training_x, training_y, dev_x = create_training_and_dev_sets()
    # Train scikit-learn naive Bayes classifier
    clf = SVC()
    clf.fit(training_x, training_y)
    # Evaluate on dev set

    dev_y_predicted = clf.predict(dev_x)


    if dev_y_predicted[0] == 0 : print("British English!")
    else: print("American English!")
