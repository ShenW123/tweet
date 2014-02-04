'''
Created on 2014-01-25

@author: Shen Wang
'''
import re
import htmlentitydefs

'''
Takes string and parses from HTML to plain text
'''
def strip_HTML(twt):
    #Removes anything within <> of HTML
    twt = re.sub('<[^<]+?>', '', twt)
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
