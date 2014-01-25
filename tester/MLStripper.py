'''
Created on 2014-01-25

@author: Shen Wang
'''
from bs4 import BeautifulSoup

class MLStripper:
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
    soup = BeautifulSoup(twt)
    return soup.get_text()