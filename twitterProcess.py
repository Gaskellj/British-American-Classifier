from nltk.corpus import twitter_samples
docs=twitter_samples.docs("tweets.20150430-223406.json")
#select the first five items
#use for-loop to print each item


with open("sentenceTrain/Tweets/British/BritishTweets.txt",'w') as w:
    with open("sentenceTrain/Tweets/American/AmericanTweets.txt",'w') as w2:
        
        for doc in docs:

            #British timezone
            if(doc['user']['utc_offset']):
                if(doc['user']['utc_offset'] == 3600):
                        w.write(' '.join(doc["text"].split()) + "\n")
                elif(doc['user']['utc_offset'] <= -18000 and doc['user']['utc_offset'] >= -36000):
                        w2.write(' '.join(doc["text"].split()) + "\n")

