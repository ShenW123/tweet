'''
Created on 2014-01-25

@author: Shen Wang
'''
from bs4 import BeautifulSoup

class MLStripper(BeautifulSoup):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)
    
def strip_tags(html):
    soup = BeautifulSoup(html)
    return soup.get_text()