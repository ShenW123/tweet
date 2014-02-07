'''
Created on 2014-01-19

@author: Shen Wang

twtt.py program takes two arguments: the input raw tweet file and the name of the output tokenized and tagged
tweet file. Use `.twt' as the extension for the output
'''

import sys #Required for cmd line arguments
import re #Requried for regex expressions
import htmlentitydefs #Required to replace &amp and other HTML terms

import NLPlib #Provided Tagging Library

tagger = NLPlib.NLPlib() #Initiliaze Tagger

'''
strip HTML
    Input: a string tweet
    Output: a string tweet without any HTML code
Takes string and parses from HTML to plain text
'''
def strip_HTML(twt):
    #Removes anything within <> of HTML
    twt = re.sub('<[^<]+?>', '', twt)
    #Takes any x given to the function and gets the unicode string of the first element of the found match
    twt = re.sub('&([^;]+);', lambda x: unichr(htmlentitydefs.name2codepoint[x.group(1)]), twt)
    return twt

'''
strip hash and links
    Input: a string tweet
    Output: a cleaner string without hashes or links
Removes #Name and @Name as well as the links starting with http or www or bbc and other sites
'''
def strip_hash_links(twt):
    #Removes only the # with anything that is #SOMETEXT
    twt = re.sub('(\#(?=\w))', '', twt)
    
    #Removes only the @ with anything that is @SOMETEXT
    twt = re.sub('(\@(?=\w))', '', twt)
    
    #Removes anything that starts with http://
    twt = re.sub('(?<=http://)(\S.+[\s])', '' , twt)
    twt = re.sub('(http://)', '' , twt)
    
    #Removes anything that starts with www.
    twt = re.sub('(?<=www\.)(\S.+[\s])', '' , twt)
    twt = re.sub('(www\.)', '' , twt)
    
    twt = re.sub('(?<=reut\.rs\/)(\S.+[\s])', '' , twt)
    twt = re.sub('(reut\.rs\/)', '' , twt)
    
    twt = re.sub('(?<=bbc\.in\/)(\S.+[\s])', '' , twt)
    twt = re.sub('(bbc\.in\/)', '' , twt)
    
    twt = re.sub('(?<=bit\.ly\/)(\S.+[\s])', '' , twt)
    twt = re.sub('(bit\.ly\/)', '' , twt)
    
    twt = re.sub('(?<=on\.cnn\.com\/)(\S.+[\s])', '' , twt)
    twt = re.sub('(on\.cnn\.com\/)', '' , twt)
    
    twt = re.sub('(?<=nyti\.ms\/)(\S.+[\s])', '' , twt)
    twt = re.sub('(nyti\.ms\/)', '' , twt)
    
    twt = re.sub('(?<=onion\.com\/)(\S.+[\s])', '' , twt)
    twt = re.sub('(onion\.com\/)', '' , twt)
    
    twt = re.sub('(?<=youtube\.com\/)(\S.+[\s])', '' , twt)
    twt = re.sub('(youtube\.com\/)', '' , twt)
    
    twt = re.sub('(?<=tinyurl\.com\/)(\S.+[\s])', '' , twt)
    twt = re.sub('(tinyurl\.com\/)', '' , twt)
    
    return twt


'''
Flattens Irregular Lists
    Input: an irregular list
    Output: a regular 1 depth list
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
End of sentence function
    Input: a string to be split into it's sentence components
    Output: a list of strings that are split into their respective sentences
'''
def EOS(twt):
    '''
    To make sure that "Sentence. Sentence?" isn't broken until end of quotations
    
    Split by quotations
    at each quotation mark know that next item in list is the inner quotation marks
    and the one after is the end quotations
    
    Thus adds all 3 into a single list and append it
    flatten afterwards in case of irregular lists
    '''
    flat_twt = []
    was_quote = 0
    twt = re.split('([^/"]*|[/"])', twt) #Splits from "[inclusive]"
    
    for index in range(len(twt)):
        if len(twt[index]) >= 1:
            #for cases of regex splitting a null or no length character
            if was_quote != 0:
                if was_quote == 1:
                    #Whenever a quote was added wait through index until done so no duplicates
                    was_quote = was_quote + 1
                else:
                    was_quote = 0
            elif twt[index][0] == '"':
                #Adds the quotation marked sentence
                flat_twt.append(twt[index] + twt[index + 1] + twt[index + 2])
                was_quote = was_quote + 1
            else:
                #Splits all other non quotation marked sentences by regular sentence endings
                split = re.split('(\S.+?[.!?])(?=\s+|$)', twt[index])
                flat_twt.append(split) 
    twt = flatten(flat_twt)
    
    '''
    Finding First and Last words
    allows for comparison of the words to determine sentence changes or abbreviations ending or not ending sentences
    '''
    firsts = []
    lasts = []
    for first_and_last in twt:
        if len(first_and_last.strip()) > 1: #To get rid of whitespace only list items or null characters
            firstword = first_and_last.strip().split()[0]
            lastword = first_and_last.strip().split()[-1]
            firsts.append(firstword)
            lasts.append(lastword)
            
    firsts.append("\n") #End of sentence to match with indexes for below
    
    '''
    
    '''
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
    Input: a list of strings that are each token to be tagged
    Output: list of tags of the strings (not!!! the token/tag)
'''
def tag(sent):
    tags = tagger.tag(sent)
    return tags

'''
To Tag
    Input: a list of strings that are each token to be tagged
    Output: a list of token/tag in that format
Tags all tokens and joins them with their tags
then retags them using postProcessor
'''
def to_tag(sentence):
        tagged = tag(sentence)
        for i in range(len(sentence)):
            sentence[i] = sentence[i] + '/' + tagged[i]
        sentence = postProcess(sentence)
        sentence = " ".join(sentence)
        return sentence

'''
Tokenization of the words
    Input: list of list of strings that are sentences
    Output: a string that is properly tagged and formatted for writing
'''
def tokenize(twt):
    tweets = []
    for sentence in twt:
        sentence = " ".join(sentence) #For sentence is a list, needs to convert to string
        sentence = sentence.strip().split()
        cleansentence = []
        for word in sentence:
            #Splitting up the word itself from punctuation and other attached items
            word = re.split('([^\w]+?)(?=\s+|$)|(?<=\$)(\S+\d|$)|(\")|(?<=\")(\w+)|(n\'t)|(\')', word)
            #([^\w]+?)(?=\s+|$) gets all non-words greedy until a space or endline (TODO: should there be |\n)
            #(?<=\$)(\S+\d|$) Looks for anything with a preceding $ and don't split up the value until the end has a non-number
            #(\") captures all quotation marks
            #(?<=\")(\w+) captures all words preceded by quotation marks
            #(n\'t) captures all n't type endings of words and splits them
            #(\') captures any ' apostrophes left not included in above capture
            clean_word = []
            for el in range(len(word)):
                if word[el] is None: #Checks for a None value type due to splitting
                    continue
                elif len(word[el]) >= 1: #Checks for if splitting resulted in a 0 length string
                    clean_word.append(word[el])
            cleansentence.append(clean_word)
        cleansentence = flatten(cleansentence)
        
        sentence = to_tag(cleansentence)
        
        tweets.append(sentence)
        
    tweets = "\n".join(tweets) #join all separate sentences by newline
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
wordlist_add(filename of the wordlist to import)
    Input: filename of wordlist which has a format of a new line between each word
    Output: A dictionary containing each word in wordlist
'''
def wordlist_add(wordlist):
    wordlist_all = {}
    filename = str(wordlist)
    wordlist_file = file(filename, "r")
    word_in_list = wordlist_file.readline()
    while word_in_list:
        word_in_list = re.sub('\n', '', word_in_list)
        wordlist_all[word_in_list] = 1;
        word_in_list = wordlist_file.readline()
    wordlist_file.close()
    return wordlist_all

'''
-------------------------------------------------Main Process Start--------------------------------------------------
'''

'''
Initialization of dictionaries to be used in post process tagging
'''
abbrall = wordlist_add("Wordlists/abbrev.english") #TODO: Change these to be more generic (eg. absolute paths to the school computers
fppall = wordlist_add("Wordlists/First-person")
sppall = wordlist_add("Wordlists/Second-person")
tppall = wordlist_add("Wordlists/Third-person")
slangall = wordlist_add("Wordlists/Slang")

'''
Argument Processing
    Input: Command line arguments where argv[0] is twtt.py and argv[1] and argv[2] are the file to read and write respectively
Ignores all other arguments
'''
# file_to_read = sys.argv[1]
# file_to_write = sys.argv[2]
files = ["tweet_test"]
# files = ["aplusk", "BarackObama", "bbcnews", "britneyspears", "CBCNews", "cnn", "justinbieber", 
#          "katyperry", "KimKardashian", "ladygaga", "neiltyson", "nytimes", "Reuters", "rihanna", "sciencemuseum", 
#          "shakira", "StephenAtHome", "taylorswift13", "TheOnion", "torontostarnews", "tweet_test"]

'''
Main Process
'''
#TODO: Change these to be more generic (to the actual lab computers paths?
for temp_placeholder in files:
    tweetfile = file("Tweets/" + temp_placeholder, "r") #TODO: change these to be actual lab computer paths
    writefile = file("Processed/" + temp_placeholder + ".twt", "w")
    
    twt = tweetfile.readline() #Initialize First Line
    writefile.write('|\n')#Initialize first tweet
    while twt:
        twt = strip_HTML(twt) #String output with HTML's removed
        twt = strip_hash_links(twt) #String output with #,@, and other links removed
        twt = EOS(twt) #List output with each element in list a separate sentence
        twt = tokenize(twt) #String output with the tweet formatted
        writefile.write(twt)
        writefile.write('\n|\n') #At end of each tweet add a | and \n to distinguish between tweets
        twt = tweetfile.readline()
    tweetfile.close()
    writefile.close()



