'''
Created on 2014-01-25

@author: Shen Wang
'''
import unittest
import MLStripper
from preprocessor import HTML_Parser

class Test_HTML(unittest.TestCase):
    '''
    test_match compares my HTML_Parser with BeautifulSoup HTML Parser and if they match then it is parsed correctly
    Input: twt (a single tweet)
    Output: Pass/Fail
    '''
    def test_match(self): 
        tweetfile = file("Tweets/tweet_test", "r")
        twt = tweetfile.readline()
        
        base = MLStripper.strip_tags(twt)
        mytweet = HTML_Parser.strip_tags(twt)
        print twt
        print base
        print mytweet
        self.assertEqual(base, mytweet, 'HTML Parsed Incorrectly')

if __name__ == "__main__":
    unittest.main()