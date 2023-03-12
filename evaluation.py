"""

Text Classification For Dialog Recognition on English and American Corpora

Author: Colby Beach, James Gaskell, Kevin Welch and Kristina Streignitz

We affirm that we have carried out my academic endeavors with full
academic honesty. Colby Beach, James Gaskell, Kevin Welch

"""


# Classifeir Evaluation Functions that we created 
# from Project 2.


##Helper functions so we don't have to repeat code##
def get_true_positives(y_pred, y_true):
    truePos = 0
    
    for prediction in range(len(y_pred)):

        if y_pred[prediction] == 1 and y_true[prediction] == 1:
            truePos += 1

    return truePos

def get_true_negatives(y_pred, y_true):
    truePos = 0
    
    for prediction in range(len(y_pred)):

        if y_pred[prediction] == 0 and y_true[prediction] == 0:
            truePos += 1

    return truePos


def get_false_negatives(y_pred, y_true):
    falseNeg = 0
    
    for prediction in range(len(y_pred)):

        if y_pred[prediction] == 0 and y_true[prediction] == 1:
            falseNeg += 1

    return falseNeg


def get_false_positives(y_pred, y_true):
    falsePos = 0
    
    for prediction in range(len(y_pred)):

        if y_pred[prediction] == 1 and y_true[prediction] == 0:
            falsePos += 1

    return falsePos



def get_accuracy(y_pred, y_true):
    """Calculate the accuracy of the predicted labels.
    y_pred: list predicted labels
    y_true: list of corresponding true labels
    """
    ## YOUR CODE HERE...        
    # print("Length: ",  len(y_pred))  
    # print("TruePos: ",  get_true_positives(y_pred, y_true))
    # print("FalseNeg: ",  get_false_negatives(y_pred, y_true))
    return (get_true_positives(y_pred, y_true) + get_true_negatives(y_pred, y_true)) / len(y_pred)

def get_precision(y_pred, y_true):
    """Calculate the precision of the predicted labels.
    y_pred: list predicted labels
    y_true: list of corresponding true labels
    """
    ## YOUR CODE HERE...
    return get_true_positives(y_pred, y_true) / (get_true_positives(y_pred, y_true) + get_false_positives(y_pred, y_true))


def get_recall(y_pred, y_true):
    """Calculate the recall of the predicted labels.
    y_pred: list predicted labels
    y_true: list of corresponding true labels
    """
    ## YOUR CODE HERE...
    return get_true_positives(y_pred, y_true) / (get_true_positives(y_pred, y_true) + get_false_negatives(y_pred, y_true))


def get_fscore(y_pred, y_true):
    """Calculate the f-score of the predicted labels.
    y_pred: list predicted labels
    y_true: list of corresponding true labels
    """
    ## YOUR CODE HERE...
    return (2 * get_precision(y_pred, y_true) * get_recall(y_pred, y_true)) / (get_precision(y_pred, y_true) + get_recall(y_pred, y_true))


def evaluate(y_pred, y_true):
    """Calculate precision, recall, and f-score of the predicted labels
    and print out the results.
    y_pred: list predicted labels
    y_true: list of corresponding true labels
    """
    ## YOUR CODE HERE...

    acc = "Accuracy: " + str(get_accuracy(y_pred, y_true) * 100) + "%\n"
    pre = "Precision: " + str(get_precision(y_pred, y_true) * 100) + "%\n"
    rec = "Recall: " + str(get_recall(y_pred, y_true) * 100) + "%\n"
    fsc = "F-score: " + str(get_fscore(y_pred, y_true) * 100) + "%"

    return acc + pre + rec + fsc


if __name__ == "__main__":
    print("Testing with the arrays: [1,1,0,0,1,0,0,1,0,0], [1,1,1,1,1,0,0,0,0,0]")
    print(evaluate([1,1,0,0,1,0,0,1,0,0], [1,1,1,1,1,0,0,0,0,0]))
