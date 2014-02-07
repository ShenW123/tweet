'''
Created on 2014-01-22

@author: Shen Wang

buildarff.py takes input -# class:file+file... ... writefile, "
'''
import attributes
import sys

#TODO: Change this to utilize sys.argv
#TODO: can you have no argument 1 if so then my code will get screwed up?

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

'''
find class
    Input: a list of all classes, files, and a filename to search for
    Output: either the fileName or a class of which the filename is a subset of
'''
def find_class(feature_class, feature_files, fileName):
    for a in range(len(feature_class)):
        if fileName in feature_class[a]:
            return fileName
        elif fileName in feature_files[a]:
            return "".join(feature_class[a])

'''
checks argument one for the -# value
    Input: the system argument 1
    Output: the 
'''
def check_arg_one(arguments):
    if ((arguments[0] == '-') & (len(arguments) > 1)): #if it begins with - and has more than just that
        tweet_number = int(arguments.split('-')[1])
        if (tweet_number < 0):
            tweet_number = 9999
    else:
        tweet_number = 9999 #Default? how do you make it ALL THE TWEETS just loop it all the time?
    return tweet_number

'''
checks arguments 2->(n-1)
    Input: the system arguments
    Output: a list of 2 lists, one containing the files, the other containing the classes (or files if no classes)
'''    
def check_arg_n(arguments):
    feature_class = []
    feature_files = []
    for index in range(len(arguments) - 2): #So can handle the + 1 to index by reducing length by 1 and skips last argument
        n = arguments[index + 1] #Skips the first index 0 for it is the buildarff.py
        n = n.split(':')
        if len(n) > 1:
            for i in range(0, len(n), 2):
                feature_class.append([n[i]])
                feature_files.append(n[i+1].split('+'))
        else:
            feature_class.append(n[0].split('+'))
            feature_files.append(n[0].split('+'))
    return [feature_class, feature_files]
    
'''
-------------------------------------------------Main Process Start--------------------------------------------------
'''
    
for argument in args: #TODO: delete this later
    sys_argv = argument

    if len(sys_argv) > 2: 
    #TODO: do i need to check this?
    #Must have at least 3 arguments 1st: Determines # of tweets, 2nd - n-1th: Determines classes and readfiles, Last: Determine writefile
        tweet_number = check_arg_one(sys_argv[1])
        features = check_arg_n(sys_argv)
        write_fileName = sys_argv[-1]
        #Arguments processed

        '''
        Initializing the ARFF file with header information
        '''
        writefile = file("ARFF/" + write_fileName + ".arff", "w") #TODO: Change this to be more generic
        
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
        for i in range(len(features[0])):
            classes.append(",".join(features[0][i]))
        writefile.write("@attribute twit {%s}\n" % (",".join(classes)))
                                             
        writefile.write("\n@data\n")
        
        
        '''
        Finding attribute values for each tweet and writing
        '''
        for file_list in features[1]:
            for fileName in file_list:
                #For each filename first build the list of tweets
                max_tweets = tweet_number
                tweetfile = file("Processed/" + fileName, "r") #TODO: change this to a more generic name
                tweet = []
                alltweets = []
                twt = tweetfile.readline() #Initialize first | of tweet
                twt = tweetfile.readline() #Initialize First Line
                while twt:
                    #If sees a |\n then there is a new tweet
                    if twt == "|\n":
                        alltweets.append(tweet)
                        max_tweets = max_tweets - 1
                        tweet = []
                    else:
                        tweet.append(twt)
                    
                    #If exceeded the number of tweets that should be read stop processing this file
                    if max_tweets > 0:
                        twt = tweetfile.readline()
                    else:
                        break;
                
                #Builds the attributes string list for every single tweet in the file
                for element in alltweets:
                    values = attributes.get_attributes("".join(element))
                    printout = ",".join(values)
                    writefile.write("%s" % printout)
                    writefile.write(",%s\n" % find_class(features[0], features[1], fileName))
                    
        tweetfile.close()
        writefile.close()
    