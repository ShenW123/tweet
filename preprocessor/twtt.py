'''
Created on 2014-01-19

@author: Shen Wang

twtt.py program takes two arguments: the input raw tweet file and the name of the output tokenized and tagged
tweet file. Use `.twt' as the extension for the output
'''

import sys
import re
import NLPlib
import setup
import HTML_Parser


tagger = NLPlib.NLPlib() #Initiliaze Tagger

'''
Identifies end of sentences and splits sentences
'''
def EOS(twt):
    
    firsts = []
    lasts = []
    twt = re.split('([^/"]*|[/"])', twt)
    was_quote = 0
    flat_twt = []
    for index in range(len(twt)):
        if len(twt[index]) >= 1:
            if was_quote != 0:
                if was_quote == 1:
                    was_quote = was_quote + 1
                else:
                    was_quote = 0
            elif twt[index][0] == '"':
                flat_twt.append(twt[index] + twt[index + 1] + twt[index + 2])
                was_quote = was_quote + 1
            else:
                split = re.split('(\S.+?[.!?])(?=\s+|$)', twt[index]) 
                flat_twt.append(split) 
    twt = flatten(flat_twt)
    
    for c in twt:
        if len(c.strip()) > 1:
            firstword = c.strip().split()[0]
            lastword = c.strip().split()[-1]
            firsts.append(firstword)
            lasts.append(lastword)
            
    firsts.append("\n") #End of sentence
    
    index = 1
    tweet = []
    sentence = []
    for i in range(len(twt)):
        if len(twt[i].strip()) > 1:
            if lasts[index - 1] in abbrall: #if its in abbreviations
                sentence.append(twt[i]) #then keep the same sentence
            elif firsts[index].islower(): #and if the first word of next sentence is lower case
                sentence.append(twt[i]) #then keep the same sentence
            else:
                sentence.append(twt[i])
                tweet.append(sentence) #end the sentence
                sentence = [] #resets sentence
            index = index + 1 #always increment index if the len >2
    return tweet

'''
Tagger System
tagger = NLPlib.NLPlib()
sent = ['tag', 'me']
tags = tagger.tag(sent)
'''
def tag(sent):
    tags = tagger.tag(sent)
    return tags

'''
Flatten
Flattens an irregular list of strings
'''
def flatten(input_list):
    output_list = []
    for element in input_list:
        if type(element) == list:
            output_list.extend(flatten(element))
        else:
            output_list.append(element)
    return output_list

'''
To Tag
Tags all words, then retags them using postProcessor
'''
def to_tag(sentence):
        tagged = tag(sentence)
        for i in range(len(sentence)):
            sentence[i] = sentence[i] + '/' + tagged[i]
        sentence = postProcess(sentence)
        sentence = " ".join(sentence)
        return sentence

'''
Tokenization
Creates the proper tokens
The output is a list of sentences of completely tagged tokens
'''
def tokenize(twt):
    tweets = []
    for sentence in twt:
        sentence = " ".join(sentence)
        sentence = sentence.strip().split()
        cleansentence = []
        for word in sentence:
            word = re.split('([^\w]+?)(?=\s+|$)|(?<=\$)(\S+\d|$)|(["])|(?<=\")(\w+)|(n\'t)|(\')', word) #need to account for 5,000... and 
            clean_word = []
            for el in range(len(word)):
                if word[el] is None:
                    continue
                elif len(word[el]) >= 1:
                    clean_word.append(word[el])
            #Possible Implementations, 1) if there is punctuation inside the word like . or comma then don't split! Else split
            #that won't account for U.S. therefore the last period splits if next word is upper and doesn't if next word is lower?
            cleansentence.append(clean_word)
        #TODO: double check edge cases
        cleansentence = flatten(cleansentence)
        sentence = to_tag(cleansentence)
        
        tweets.append(sentence)
        
    tweets = "\n".join(tweets)
    return tweets

'''
Tagger Post Processing
Input: Tagged sentence split into list of tokens
Output: Retagged sentence
'''
def postProcess(sentence):
    sentence = change_tag(sentence, fppall, 'PRP', 'FPRP') #Changes all first person pronouns
    sentence = change_tag(sentence, sppall, 'PRP', 'SPRP') #Changes all second person pronouns
    sentence = change_tag(sentence, tppall, 'PRP', 'TPRP') #Changes all third person pronouns
    sentence = change_tag(sentence, slangall, '', 'SLANG') #Appropriate changes for any word that matches SLANG terms
    return sentence

'''
Change Tag
Input: Tagged sentence split into list of tokens, A Dictionary to check values, a Tag that you want to replace, and an End_Tag
Output: Retagged sentence where tag is changed to end_tag whenever the word before tag matches with something in check dictionary
'''
def change_tag(sentence, check, tag, end_tag):
    post_sentence = []
    for word in sentence:
        m = re.match('(\S+)(?=/%s)'%tag, word)
        if m:
            found = m.group(1)
            if found.lower() in check:
                word = found + '/' + end_tag
        post_sentence.append(word)
    return post_sentence

'''
-------------------------------------------------Main Process Start--------------------------------------------------
'''

'''
Argument Processing
To take the 2 arguments required
If given more arguments, don't care about them
'''
# file_to_read = sys.argv[1]
# file_to_write = sys.argv[2]
files = ["tweet_test"]
files = ["aplusk", "BarackObama", "bbcnews", "britneyspears", "CBCNews", "cnn", "justinbieber", 
         "katyperry", "KimKardashian", "ladygaga", "neiltyson", "nytimes", "Reuters", "rihanna", "sciencemuseum", 
         "shakira", "StephenAtHome", "taylorswift13", "TheOnion", "torontostarnews", "tweet_test"]


'''
Setup all dictionaries needed
'''
abbrall = setup.add_abbr()
fppall = setup.add_fpp()
sppall = setup.add_spp()
tppall = setup.add_tpp()
slangall = setup.add_slang()

'''
Main Process
'''
#TODO: Change these to be more generic (to the actual lab computers paths?
for c in files:
    tweetfile = file("Tweets/" + c, "r")
    writefile = file("Processed/" + c + ".twt", "w")

    # tweetfile = file("Tweets/tweet_test", "r")
    # writefile = file("Processed/" + "tweet_test.twt", "w")
    
    twt = tweetfile.readline() #Initialize First Line
    writefile.write('|\n')#Initialize first tweet
    while twt:
        twt = HTML_Parser.strip_HTML(twt) #HTML remover
        twt = HTML_Parser.strip_hash_links(twt) #Hash and Links Removal
        twt = EOS(twt) #Twt is now a list of sentences
        twt = tokenize(twt) #Twt is a list of sentences that is now a list of processed tokens
        writefile.write(twt)
        writefile.write('\n|\n') #At end of each tweet add a | and \n to distinguish between tweets
        twt = tweetfile.readline() #Read next tweet
    tweetfile.close()
    writefile.close()



