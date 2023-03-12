"""

Text Classification For Dialog Recognition on English and American Corpora

Author: Colby Beach, James Gaskell, Kevin Welch and Kristina Streignitz

We affirm that we have carried out my academic endeavors with full
academic honesty. Colby Beach, James Gaskell, Kevin Welch

"""


# Function that gets the NLTKT twitter data 
# and outputs it into its own sentence files just as 
# the sentence_split.py file does.

from nltk.corpus import twitter_samples
docs=twitter_samples.docs("tweets.20150430-223406.json")

with open("sentenceTrain/Tweets/British/BritishTweets.txt",'w') as w:
    with open("sentenceTrain/Tweets/American/AmericanTweets.txt",'w') as w2:
        
        for doc in docs:

            # Checks to see which time zone the user is in so we can distinguish between 
            # American Tweets and British Tweets
            
            if(doc['user']['utc_offset']):
                #British
                if(doc['user']['utc_offset'] == 3600):
                        w.write(' '.join(doc["text"].split()) + "\n")
                #American
                elif(doc['user']['utc_offset'] <= -18000 and doc['user']['utc_offset'] >= -36000):
                        w2.write(' '.join(doc["text"].split()) + "\n")

