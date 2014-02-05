'''
Created on 2014-01-22

@author: Shen Wang
'''
import attributes
import sys

#TODO: Change this to utilize sys.argv

args = []

celebrity = ["-1000", "BarackObama.twt+StephenAtHome.twt+aplusk.twt+KimKardashian.twt+neiltyson.twt+shakira.twt", "celebrity"]
news = ["-1000", "CBCNews.twt+cnn.twt+nytimes.twt+Reuters.twt+TheOnion.twt+torontostarnews.twt", "news"]
popstars = ["-1000", "justinbieber.twt+ladygaga.twt+britneyspears.twt+katyperry.twt+rihanna.twt+taylorswift13.twt", "popstars"]
newsvspopstars = ["-1000", "news:CBCNews.twt+cnn.twt+nytimes.twt+Reuters.twt+TheOnion.twt+torontostarnews.twt", 
"pop:justinbieber.twt+ladygaga.twt+britneyspears.twt+katyperry.twt+rihanna.twt+taylorswift13.twt", "newsvspopstars"]

args.append(celebrity)
args.append(news)
args.append(popstars)
args.append(newsvspopstars)

#news = "news:bbcnews.twt+CBCNews.twt+cnn.twt+nytimes.twt+Reuters.twt+TheOnion.twt+torontostarnews.twt+aplusk.twt"
#popstars = "pop:justinbieber.twt+ladygaga.twt+britneyspears.twt+katyperry.twt+KimKardashian.twt+shakira.twt+rihanna.twt+taylorswift13.twt"
#sys_argv = ["-700", news, popstars, "newsvspopstars"] #sample argv. Replace sys_argv with sys.argv in real situation

def find_class(feature_class, feature_files, fileName):
    for a in range(len(feature_class)):
        if fileName in feature_class[a]:
            return fileName
        elif fileName in feature_files[a]:
            return "".join(feature_class[a])

for argument in args:
    sys_argv = argument

            
    if len(sys_argv) > 2: #Must have at least 3 arguments 1st: Determines # of tweets, 2nd - n-1th: Determines classes and readfiles, Last: Determine writefile
        if ((sys_argv[0][0] == '-') & (len(sys_argv[0]) > 1)): #if it begins with - and has more than just that
            tweet_number = int(sys_argv[0].split('-')[1])
            if (tweet_number < 0):
                tweet_number = 9999
        else:
            tweet_number = 9999 #Default? how do you make it ALL THE TWEETS just loop it all the time?
        
        feature_class = []
        feature_files = []
        for index in range(len(sys_argv) - 2): #So can handle the + 1 to index by reducing length by 1 and skips last argument
            n = sys_argv[index + 1] #So skips the first index 0
            n = n.split(':')
            if len(n) > 1:
                for i in range(0, len(n), 2):
                    feature_class.append([n[i]])
                    feature_files.append(n[i+1].split('+'))
            else:
                feature_class.append(n[0].split('+'))
                feature_files.append(n[0].split('+'))
                
        write_fileName = sys_argv[-1]
    
    #next n arguments are in format of class:tweetfile+tweetfile+... each
    #last argument is output arff
    
    writefile = file("ARFF/" + write_fileName + ".arff", "w")
    
    writefile.write('@relation twit_classification\n\n') #Initialize first line
    
    attribute_list = ["first_person_pronouns", "numeric", "second_person_pronouns", "numeric", "thrid_person_pronouns", "numeric",
                  "coordinating_conjunctions", "numeric", "past_tense_verbs", "numeric", "future_tense_verbs", "numeric", "commas", "numeric", "colons_semicolons", "numeric",
                  "dashes", "numeric", "parentheses", "numeric", "ellipses", "numeric", "incorrect_ellipses", "numeric", "common_singular_nouns", "numeric", "common_plural_nouns", "numeric", "proper_singular_nouns", "numeric"
                  , "proper_plural_nouns", "numeric", "adverb", "numeric", "adverb_comparative", "numeric",
                  "adverb_superlative", "numeric", "wh_words", "numeric", "slang", "numeric", "all_caps_words", "numeric",
                  "number_of_sentences", "numeric", "average_sentence_length", "numeric", "alltokens_not_punctuation_length", "numeric"
                   ]
    
    for index in range(0, len(attribute_list), 2):
        line = "@attribute " + attribute_list[index] +" "+ attribute_list[index + 1] + "\n"
        writefile.write(line)
    
    classes = []
    for i in range(len(feature_class)):
        classes.append(",".join(feature_class[i]))
    writefile.write("@attribute twit {%s}\n" % (",".join(classes)))
                                         
    writefile.write("\n") #separator
    writefile.write("@data\n")
    
    for file_list in feature_files:
        for fileName in file_list:
            max_tweets = tweet_number
            tweetfile = file("Processed/" + fileName, "r")
            tweet = []
            alltweets = []
            twt = tweetfile.readline() #Initialize first | of tweet
            twt = tweetfile.readline() #Initialize First Line
            while twt:
                if twt == "|\n":
                    alltweets.append(tweet)
                    max_tweets = max_tweets - 1
                    tweet = []
                else:
                    tweet.append(twt)
                
                if max_tweets > 0:
                    twt = tweetfile.readline() #Read next tweet
                else:
                    break;
            
            for element in alltweets:
                values = attributes.get_attributes("".join(element))
                printout = ",".join(values)
                writefile.write("%s" % printout)
                writefile.write(",%s\n" % find_class(feature_class, feature_files, fileName))
                
    tweetfile.close()
    writefile.close()
    
    
    
    