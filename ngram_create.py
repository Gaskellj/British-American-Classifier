"""

Text Classification For Dialog Recognition on English and American Corpora

Author: Colby Beach, James Gaskell, Kevin Welch and Kristina Streignitz

We affirm that we have carried out my academic endeavors with full
academic honesty. Colby Beach, James Gaskell, Kevin Welch

"""

import os
import json

def start_pad(c):
    ''' Returns a padding string of length c to append to the front of text
        as a pre-processing step to building n-grams. c = n-1 '''
    return '~' * c

def ngrams(c, text):
    ''' Returns the ngrams of the text as tuples where the first element is
        the length-c context and the second is the character '''
    ngramArray = []
    for count in range(0,len(text)):
        context = c - count
        string = ""
        tempArray = []
        if context > 0:
            string += (start_pad(context))
            for i in range (0,(c-context)):
                string += text[i]
        else:
            for i in range(c,0,-1):
                string += text[count-i]
        tempArray.append(string)
        tempArray.append(text[count])
        ngramArray.append(tempArray)

    return ngramArray

class NgramModel(object):
    ''' A basic n-gram model using add-k smoothing '''

    def __init__(self, c, k):
        self.context = c
        self.k = k
        self.context_dictionary = {}
        self.NgramDict = {}
        self.vocabDict = []

    def get_vocab(self):
        ''' Returns the set of characters in the vocab '''
        for character in self.NgramDict:
            if (character[1]) not in self.vocabDict:
                self.vocabDict.append(character[1])

    def update_dictionary(self,context):
        if context in self.context_dictionary:
            self.context_dictionary[context] += 1
        else:
            self.context_dictionary[context] = 1

    def update(self, text):
        Ngrams = ngrams(self.context,text)
        for n in Ngrams:
            if tuple(n) in self.NgramDict:
                self.NgramDict[tuple(n)] += 1
            else:
                self.NgramDict[tuple(n)] = 1
            self.update_dictionary(n[0])
        myKeys = list(self.context_dictionary.keys())
        myKeys.sort()
        self.context_dictionary = {i: self.context_dictionary[i] for i in myKeys}
        self.get_vocab()
        self.vocabDict.sort()


if __name__ == "__main__":
    #Labeling American
    # create_labels("", "", 1)

    # #Labeling British 
    # create_labels("", "", 0)
    American = NgramModel(4,0)
    directory = "rawData/American"
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if f.endswith(".txt"):
            with open(f, encoding='utf-8', errors='ignore') as f:
                for line in f:
                    American.update(line)
    
    with open(directory + "/NgramCounts.txt", 'w') as file:
        file.write(json.dumps(American.context_dictionary))

    
    British = NgramModel(4,0)
    directory = "rawData/British"
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if f.endswith(".en"):
            with open(f, encoding='utf-8', errors='ignore') as f:
                for line in f:
                    British.update(line)

    with open(directory + "/NgramCounts.txt", "w") as file:
        file.write(json.dumps(British.context_dicitonary))