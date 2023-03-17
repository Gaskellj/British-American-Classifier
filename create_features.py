"""

Text Classification For Dialect Recognition on English and American Corpora

Author: Colby Beach, James Gaskell, Kevin Welch and Kristina Streignitz

We affirm that we have carried out my academic endeavors with full
academic honesty. Colby Beach, James Gaskell, Kevin Welch

"""



# This file is our main area to create all of our features
# to run our classifier. We choose 6 different features as shown below,
# including one that was given to us by Profesor Streignitz in the movie classification
# starter code.

from collections import Counter

#Gets all designated American Spellings
amerWords = []
my_file = open("spellingList/AmericanSpelling.txt", "r")
data = my_file.read()
amerWords.extend(data.split("\n"))
my_file.close()

#Gets all designated British Spellings
britWords = []
my_file = open("spellingList/BritishSpelling.txt", "r")
data = my_file.read()
britWords.extend(data.split("\n"))
my_file.close()

#Gets all designated American Slang Words
amerSlang = []
my_file = open("slangList/americanSlang.txt", "r")
data = my_file.read()
amerWords.extend(data.split("\n"))
my_file.close()

#Gets all designated British Slang Words
britSlang = []
my_file = open("slangList/britishSlang.txt", "r")
data = my_file.read()
britWords.extend(data.split("\n"))
my_file.close()


def create_features(sentence, vocab):
    features = [] 

    #Given feature from initial movie review classifier 
    word_counts = Counter(sentence)
    features.extend([int(word_counts[w] > 0) for w in vocab])
    

    #Adding our created features (as defined in the functions below)
    features.extend(checkSpellings(sentence))
    features.extend(checkSlang(sentence))
    features.extend(finalThree(sentence))
    features.append(checkApostrophes(sentence))
    features.append(checkDoubleChar(sentence))

    return features


# We found Americans more likely to conjugate words, therefore more apostrophes could be preent 
def checkApostrophes(sentence):
    apostrapheCount = 0
    for char in sentence:
        if char == "'":
            apostrapheCount += 1
    return apostrapheCount

# British written words tend to contain more double characters due to differences in pronunciation
def checkDoubleChar(sentence):
    sentence.split(" ")
    doubleCharCount = 0
    for word in sentence:
        for i in range (0, len(word)-1):
            if word[i] == word[i+1]:
                doubleCharCount += 1
    return doubleCharCount


#Checks last three letters for a certain suffix 
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


#Checks if there are any predefiined slang words for either dialect
def checkSlang(sentence):
    british = 0
    american = 0
    for word in sentence.split():
        if word.title() in amerSlang:
            american += 1
        elif word.title() in britSlang:
            british += 1
    
    return [british, american]


#Checks if there are any predefiined spellings for either dialect
def checkSpellings(sentence):
    
    british = 0
    american = 0

    for word in sentence.split():
        if word.lower() in amerWords:
            american += 1
        elif word.lower() in britWords:
            british += 1
    
    return [british, american]