"""

Text Classification For Dialog Recognition on English and American Corpora

Author: Colby Beach, James Gaskell, Kevin Welch and Kristina Streignitz

We affirm that we have carried out my academic endeavors with full
academic honesty. Colby Beach, James Gaskell, Kevin Welch

"""


#Gets the twitter data and outputs it into its own sentence files


from nltk.corpus import twitter_samples
docs=twitter_samples.docs("tweets.20150430-223406.json")

with open("sentenceTrain/Tweets/British/BritishTweets.txt",'w') as w:
    with open("sentenceTrain/Tweets/American/AmericanTweets.txt",'w') as w2:
        
        for doc in docs:

            #British timezone
            if(doc['user']['utc_offset']):
                if(doc['user']['utc_offset'] == 3600):
                        w.write(' '.join(doc["text"].split()) + "\n")
                elif(doc['user']['utc_offset'] <= -18000 and doc['user']['utc_offset'] >= -36000):
                        w2.write(' '.join(doc["text"].split()) + "\n")

