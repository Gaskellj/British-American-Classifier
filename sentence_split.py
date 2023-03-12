"""

Text Classification For Dialog Recognition on English and American Corpora

Author: Colby Beach, James Gaskell, Kevin Welch and Kristina Streignitz

We affirm that we have carried out my academic endeavors with full
academic honesty. Colby Beach, James Gaskell, Kevin Welch

"""
def split_sentence(readFile, writeFile):
    with open(writeFile,'w') as w:
        with open(readFile,'r') as f:
            for line in f:
                for word in line.split("."):
                    w.write(word.strip().replace('\n', ' ').replace('\r', '') + "\n")


if __name__ == "__main__":
    #Labeling American

    split_sentence("rawData/American/sorcerer-stone.txt", "sentenceTrain/America/sorcerer-stone.txt")

    #Labeling British 
    # create_labels("rawData/British/ep-00-02-02.en", "britishSentences.txt", "0")
    
    