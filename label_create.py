

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
    