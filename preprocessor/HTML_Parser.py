'''
Created on 2014-01-25

@author: Shen Wang
'''
import re
import htmlentitydefs

class HTML_Parser:
    def __init__(self):
        self.reset()
        self.d = []
    def handle_data(self, twt):
        self.d.append(twt)
    def get_data(self):
        return ''.join(self.d)
    
def strip_tags(twt):
    '''
    Takes string and parses from HTML to plain text
    '''
    #Removes anything within <> of HTML
    twt = re.sub('(<.+>)', '', twt)
    #Use <[^<]+?> (which preserves the text in the links) or <.+> which eliminates them all
    #Takes any x given to the function and gets the unicode string of the first element of the found match
    twt = re.sub('&([^;]+);', lambda x: unichr(htmlentitydefs.name2codepoint[x.group(1)]), twt)
    return twt