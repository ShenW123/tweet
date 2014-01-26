'''
Created on 2014-01-19

@author: Shen Wang


twtt.py program takes two arguments: the input raw tweet file and the name of the output tokenized and tagged
tweet file. Use `.twt' as the extension for the output
'''
import HTML_Parser
import hash_links

'''
Argument Processing
To take the 2 arguments required
'''




'''
File Reading
Takes the raw tweet file and reads it into a list to process
'''
alltwt = [] #List with all tweets
#TODO: Create a Sentence or Tweets Structure
#Opens a File
tweetfile = file("Tweets/tweet_test", "r")
twt = tweetfile.readline() #Initialize First Line
while twt:
    twt = tweetfile.readline()
    twt = HTML_Parser.strip_tags(twt) #HTML remover
    twt = hash_links.strip_hash_links(twt)
    alltwt.append(twt)
tweetfile.close()
for tweet in alltwt:
    print tweet


'''
HTML remover
Removes all HTML Tags from the raw tweets

'''


'''
Sentence Breakdown
Changes each tweet to its sentence components so each word is separated
Identifies end of sentences and splits sentences

'''


'''
Tagger Formatter
Creates a formated tweet to be inputed into the tagger
'''

'''
Tagger Post Processing
Takes output tagged file and adds .... TODO: Other post processes

'''