'''
Created on 2014-01-19

@author: Shen Wang


twtt.py program takes two arguments: the input raw tweet file and the name of the output tokenized and tagged
tweet file. Use `.twt' as the extension for the output
'''
import re

'''
Argument Processing
To take the 2 arguments required
'''




'''
File Reading
Takes the raw tweet file and reads it into a list to process
'''

#Opens a File
#TODO: Create an iterative file opener that goes through all files in folder
tweetfile = file("Tweets/tweet_test", "r")
twt = tweetfile.readline() #Initialize First Line
"""while twt:
    print twt
    twt = tweetfile.readline()
tweetfile.close()"""


'''
HTML remover
Removes all HTML Tags from the raw tweets

'''

#method using regex developed by self
print twt
twt = re.sub('(<[^<]+?>)', '', twt) # we want to remove ALL of the html tag + everything inside for usually useless
print twt



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