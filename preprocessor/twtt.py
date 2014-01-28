'''
Created on 2014-01-19

@author: Shen Wang


twtt.py program takes two arguments: the input raw tweet file and the name of the output tokenized and tagged
tweet file. Use `.twt' as the extension for the output
'''
import re
import NLPlib
import htmlentitydefs

'''
Argument Processing
To take the 2 arguments required
'''
#TODO:Argument Processing
'''
File Reading
Takes the raw tweet file and reads it
'''
#TODO:File Reading

'''
Takes string and parses from HTML to plain text
'''
def strip_HTML(twt):
    #Removes anything within <> of HTML
    twt = re.sub('(<.+>)', '', twt)
    #Use <[^<]+?> (which preserves the text in the links) or <.+> which eliminates them all
    #Takes any x given to the function and gets the unicode string of the first element of the found match
    twt = re.sub('&([^;]+);', lambda x: unichr(htmlentitydefs.name2codepoint[x.group(1)]), twt)
    return twt

'''
Removes #Name and @Name as well as the links starting with http or www or bbc and etc
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
    
    twt = re.sub('(?<=bit\.ly\/)(\S.+[\s])', '' , twt)
    twt = re.sub('(bit\.ly\/)', '' , twt)
    
    twt = re.sub('(?<=on\.cnn\.com\/)(\S.+[\s])', '' , twt)
    twt = re.sub('(on\.cnn\.com\/)', '' , twt)
    
    twt = re.sub('(?<=nyti\.ms\/)(\S.+[\s])', '' , twt)
    twt = re.sub('(nyti\.ms\/)', '' , twt)
    
    twt = re.sub('(?<=onion\.com\/)(\S.+[\s])', '' , twt)
    twt = re.sub('(onion\.com\/)', '' , twt)
    
    return twt


'''
Identifies end of sentences and splits sentences
'''
def EOS(twt):

    twt = re.split('(\S.+?[.!?"])(?=\s+|$)', twt) #End of Sentence Splitter (Does not account for U.S. and other abbreviations stuff)
    #TODO: Check through list to find abbreviation, if abbreviation is found then check next and see if there is a capital letter
    return twt

'''
Tokenization
Creates the proper tokens
'''
def tokenize(twt):
    for c in twt:
        c = c.strip().split()
        for a in c:
            a = re.split('(\s?[.!?",/\'])', a) #This doesn't account for cases like U.S. where I wan't it to stay together and paid $10,000 and other stuff
            #TODO: improve this splitting
            print a
    return twt

'''
Tagger System
tagger = NLPlib.NLPlib()
sent = ['tag', 'me']
tags = tagger.tag(sent)
'''
def tag(sent):
    tagger = NLPlib.NLPlib()
    tags = tagger.tag(sent)
    return tags

'''
Tagger Post Processing
Takes output tagged file and adds .... 
'''
#TODO: Other post processes


'''
Main Process
'''
#Opens a File
tweetfile = file("Tweets/tweet_test", "r")
twt = tweetfile.readline() #Initialize First Line
while twt:
    twt = strip_HTML(twt) #HTML remover
    twt = strip_hash_links(twt) #Hash and Links Removal
    twt = EOS(twt) #twt is now a list of sentences
    twt = tokenize(twt) #twt is now a
    print twt
    twt = tweetfile.readline()
tweetfile.close()



