'''
Created on 2014-01-25

@author: Shen Wang
'''
import unittest
import MLStripper
from preprocessor import HTML_Parser

class Test_HTML(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    '''
    Want a method to test my html parser with the builtin html parser
    '''
    def test_match(self): 
        #TODO: Implement test to run across all the tweets not just one
        #TODO: Implement better error codes?
        #TODO: Get file from elsewhere
        tweetfile = file("Tweets/tweet_test", "r")
        twt = tweetfile.readline()
        base = MLStripper.strip_tags(twt)
        mytweet = HTML_Parser.strip_tags(twt) #I think the HTML parser is incorrect... it doesn't change &amp; into ampersands
        print twt
        print base
        print mytweet
        self.assertEqual(base, mytweet, 'HTML Parsed Incorrectly')

if __name__ == "__main__":
    unittest.main()