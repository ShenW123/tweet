'''
Created on 2014-01-29

@author: Shen Wang
'''
import re
'''
Tagger Post Processing
Input: Tagged sentence split into list of tokens
Output: Retagged sentence
'''
def postProcess(sentence):
    sentence = find_First_Person_Pronouns(sentence)
    return sentence

'''
Finding First Person Pronouns
Input: Tagged sentence split into list of tokens
Output: Retagged sentence where first person pronouns becomes
/FPRP
'''
def find_First_Person_Pronouns(sentence, dict, tag, end_tag):
    post_sentence = []
    for word in sentence:
        m = re.match('(\S+)(?=/%s)'%tag, word)
        if m:
            found = m.group(1)
            if found.lower() in dict:
                word = found + '/' + end_tag
        post_sentence.append(word)
    return post_sentence
