"""

Text Classification For Dialog Recognition on English and American Corpora

Author: Colby Beach, James Gaskell, Kevin Welch and Kristina Streignitz

We affirm that we have carried out my academic endeavors with full
academic honesty. Colby Beach, James Gaskell, Kevin Welch

"""
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

import random
import numpy as np
import os 

from evaluation import evaluate
from create_features import create_features
from collections import Counter

#Creates the training and dev sets
def create_training_and_dev_sets(inputTrue):

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


    #Not actually needed if inputTrue
    dev_selection = random.sample(range(0, len(sentences)), 2000)

    if inputTrue:
        dev_reviews = [input("Enter a sentence:")]
        print("Predicting...")
    else:
        dev_reviews = [sentences[i] for i in dev_selection]

    training_reviews = [sentences[i] for i in range(len(sentences)) if i not in dev_selection]

    training_word_counts = Counter([w.lower() for review in training_reviews for w in review])
    vocab = [word_count[0] for word_count in training_word_counts.most_common(2000)]

    training_x = np.array([create_features(r, vocab) for r in training_reviews])
    dev_x = np.array([create_features(r, vocab) for r in dev_reviews])

    training_y = np.array([labels[i] for i in range(len(labels)) if i not in dev_selection])

    #Not actually needed if inputTrue
    dev_y = np.array([labels[i] for i in dev_selection])

    return training_x, training_y, dev_x, dev_y



#Runs the classifier on the dev data
def runClassifier(inputTrue):
    training_x, training_y, dev_x, dev_y = create_training_and_dev_sets(inputTrue)
    # Train scikit-learn naive Bayes classifier
    clf = SVC()
    clf.fit(training_x, training_y)
    # Evaluate on dev set

    dev_y_predicted = clf.predict(dev_x)

    if inputTrue:
        if dev_y_predicted[0] == 0 : print("British English!")
        else: print("American English!")
    else:
        print(evaluate(dev_y_predicted, dev_y))



if __name__ == "__main__":

    #Use true as a parameter if you want to enter an input
    #Use false as a parameter if you want to see evaluation stats
    runClassifier(False)


