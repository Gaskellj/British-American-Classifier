"""Named Entity Recognition as a classification task.

Author: Colby Beach, James Gaskell, Kevin Welch and Kristina Streignitz

We affirm that we have carried out my academic endeavors with full
academic honesty. Colby Beach, James Gaskell, Kevin Welch

Complete this file for part 1 of the project.
"""


def create_labels(readFile, writeFile, label):
    writeFile.write("WORD\tLABEL\n")
    with open(readFile,'r') as f:
        for line in f:
            for word in line.split():
                 writeFile.write(word +"\t" + label + "\n")


if __name__ == "__main__":
    #Labeling American
    # create_labels("", "", 1)

    # #Labeling British 
    # create_labels("", "", 0)
    print("Hey!")
    