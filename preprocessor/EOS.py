'''
Created on 2014-01-27

@author: Shen Wang
'''
import re

class hash_links():
    '''
    classdocs
    '''
    def __init__(self):
        self.reset()
        self.d = []
    def handle_data(self, twt):
        self.d.append(twt)
    def get_data(self):
        return ''.join(self.d)
    
def find_EOS(twt):
    twt = re.split('(\S.+?[.!?"])(?=\s+|$)', twt) #End of Sentence Splitter (Does not account for U.S. and other abbreviations stuff)
    #TODO: Check through list to find abbreviation, if abbreviation is found then check next and see if there is a capital letter
    return twt