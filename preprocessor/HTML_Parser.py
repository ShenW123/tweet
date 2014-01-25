'''
Created on 2014-01-25

@author: Shen Wang
'''
import re
import htmlentitydefs

class HTML_Parser:
    '''
    classdocs
    '''
    def __init__(self):
        self.reset()
        self.data = []
    def handle_data(self, twt):
        self.data.append(twt)
    def get_data(self):
        return ''.join(self.data)
    
def strip_tags(twt):
    #Takes anything within the <> brackets and removes it
    twt = re.sub('(<[^<]+?>)', '', twt)
    #Takes any x given to the function and gets the unicode string of the first element of the found match
    twt = re.sub('&([^;]+);', lambda x: unichr(htmlentitydefs.name2codepoint[x.group(1)]), twt)
    return twt