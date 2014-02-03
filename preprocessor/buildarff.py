'''
Created on 2014-02-02

@author: Shen Wang
'''
import attributes
import sys


sys_argv = ["-500", "class:tweet_test.twt", "tweet_test"] #sample argv. Replace sys_argv with sys.argv in real situation

if len(sys_argv) > 2: #Must have at least 3 arguments 1st: Determines # of tweets, 2nd - n-1th: Determines classes and readfiles, Last: Determine writefile
    if ((sys_argv[0][0] == '-') & (len(sys_argv[0]) > 1)): #if it begins with - and has more than just that
        tweet_number = int(sys_argv[0].split('-')[1])
        if (tweet_number < 0 | tweet_number > 1000):
            tweet_number = 1000
    else:
        tweet_number = 1000 #Default? how do you make it ALL THE TWEETS
    
    for index in range(len(sys_argv) - 2): #So can handle the + 1 to index by reducing length by 1 and skips last argument
        n = sys_argv[index + 1] #So skips the first index 0
        n = n.split(':')
        if len(n) > 1:
            feature_class = n[0]
            feature_files = n[1].split('+')
        else:
            feature_files = n[0].split('+')
            
    write_fileName = sys_argv[-1]

#next n arguments are in format of class:tweetfile+tweetfile+... each
#last argument is output arff



#TODO: need a way of giving it a feature of which tweet it came from after figuring out how to separate the tweets by which tweet they came from
    
writefile = file("ARFF/" + write_fileName + ".arff", "w")

writefile.write('@relation twit_classification\n\n') #Initialize first line #TODO: What is this relation? is it the class?

attribute_list = {"first_person_pronouns":"numeric", "second_person_pronouns": "numeric", "thrid_person_pronouns": "numeric",
              "coordinating_conjunctions": "numeric", "past_tense_verbs": "numeric", "commas": "numeric", "colons_semicolons": "numeric",
              "dashes": "numeric", "parentheses": "numeric", "common_singular_nouns": "numeric", "common_plural_nouns": "numeric", "proper_singular_nouns": "numeric"
              , "proper_plural_nouns": "numeric", "adverb": "numeric", "adverb_comparative": "numeric",
              "adverb_superlative": "numeric", "wh_words": "numeric", "particle": "numeric"
               }
for key in attribute_list:
    line = "@attribute " + key +" "+ attribute_list.get(key) + "\n"
    writefile.write(line)

writefile.write("\n") #separator
writefile.write("@data\n")

for fileName in feature_files:
    tweetfile = file("Processed/" + fileName, "r")
    tweet = []
    alltweets = []
    twt = tweetfile.readline() #Initialize first | of tweet
    twt = tweetfile.readline() #Initialize First Line
    while twt:
        if twt == "|\n":
            alltweets.append(tweet)
            tweet = []
        else:
            tweet.append(twt)
        twt = tweetfile.readline() #Read next tweet
    
    for element in alltweets:
        values = attributes.get_attributes(str(element)) #TODO: Can str(list) have bad stuff happen?
        writefile.write(values[0]) #Intializes first value
        del values[0] #Deletes it so doesn't affect forloop
        for index in range(len(values)):
            writefile.write(',') #comma first so the string won't end in a comma
            writefile.write(values[index])
        writefile.write('\n') #newline at end of each
            

writefile.write('\n') #newline at end of file?
tweetfile.close()
writefile.close()
    
    

    
    
    
    