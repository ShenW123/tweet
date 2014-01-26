'''
Created on 2014-01-25

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
    
def strip_hash_links(twt):
    '''
    Removes #Name and @Name as well as the links starting with http or www or bbc and etc
    '''
    #Removes only the # with anything that is #SOMETEXT
    twt = re.sub('(#(?=w))', '', twt)
    
    #Removes only the @ with anything that is @SOMETEXT
    twt = re.sub('(@(?=w))', '', twt)
    
    #Removes anything that starts with http://
    twt = re.sub('((?<=http://)[^/w]+? )', '' , twt)
    twt = re.sub('(http://)', '' , twt)
    
    #Removes anything that starts with www.
    twt = re.sub('((?<=www\.)[^/w]+? )', '' , twt)
    twt = re.sub('(www\.)', '' , twt)
    
    #Removes anything that starts with www.
    twt = re.sub('((?<=reut\.rs\/)[^/w]+? )', '' , twt)
    twt = re.sub('(reut\.rs\/)', '' , twt)
    
    #Removes anything that starts with www.
    twt = re.sub('((?<=bit\.ly\/)[^/w]+? )', '' , twt)
    twt = re.sub('(bit\.ly\/)', '' , twt)
    
    #Removes anything that starts with www.
    twt = re.sub('((?<=on\.cnn\.com\/)[^/w]+? )', '' , twt)
    twt = re.sub('(on\.cnn\.com\/)', '' , twt)
    
    #Removes anything that starts with www.
    twt = re.sub('((?<=nyti\.ms\/)[^\t\n\r\f\v]+? )', '' , twt)
#     twt = re.sub('(nyti\.ms\/)', '' , twt)
    
    #Removes anything that starts with www.
    twt = re.sub('((?<=onion\.com\/)[^/w]+? )', '' , twt)
#     twt = re.sub('(onion\.com\/)', '' , twt)

    return twt
        