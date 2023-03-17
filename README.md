# Text Classification For Dialog Recognition on English and American Corpora

## Authors - Colby Beach, Kevin Welch, James Gaskell

We affirm that we have carried out my academic endeavors with full
academic honesty. Colby Beach, James Gaskell, Kevin Welch

## Data

Data containing the State of the Union Address was used for american-dialect training data. 
This data is available [here](https://www.nltk.org/nltk_data/) under the 40th subsection labelled
C-Span State of the Union Address Corpus. Another corpus was used for the british-dialect from this 
link called Sample European Parliament Proceedings Parallel Corpus which is labelled as the 31st subsection. 

A corpus of tweets was downloaded using the same link ([here](https://www.nltk.org/nltk_data/)) under the 41st 
subsection. This data was split using timezones to separate british and american tweets respectively. 

A txt file containing a British and American edition of the first Harry Potter novel was also used. The british
edition is available [here](https://www.academia.edu/40801338/Bloomsbury_HP_1_Harry_Potter_and_the_Philosophers_Stone)
and the American version can be found here 
[here](https://www.academia.edu/39183542/J_K_Rowling_HP_1_Harry_Potter_and_the_Sorcerers_Stone). 

We have decided to provide the sentenceTrain folder containing the data above as the data was not provided in 
the necessary format. 

## Code

### [british_american_classifier.py](british_american_classifier.py)

The british_american_classifier is the main file for this project.

There are 2 ways to run this classifier. 

1. If one is looking to classify a document or segment of text, set the boolean in the main function to True. A prompt
will appear to enter a sentence. This sentence will be analyzed and classified as either British English or American 
English. 
   
2. To see the evaluation metrics for the dialect classifier, set the boolean in the main function of 
british_american_classifier to False and run the code. The classifier will use available data to train and test


### Other Files

1. [create_features.py](create_features.py): Seperate file that holds our functions to create the features for our classifier. 

2. [evaluation.py](evaluation.py): Our evaluation class from Project 2.

3. [twitterProcess.py](twitterProcess.py): Class which gets Twitter Corpus from NLTK and outputs it into its own sentence files just as the sentence_split.py file does.

4. [sentence_split.py](sentence_split.py): Takes a text file and seperates each sentence into a new line in a new file. 

5. slangList directory: Contains lists of common slang words for British vs American English.

6. spellingList directory: Contains lists of common spellings for British vs American English.

7. sentenceTrain directory: Contains our processed data that we used to train / dev. 
