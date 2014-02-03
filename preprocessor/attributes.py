'''
Created on 2014-02-02

@author: Shen Wang
'''
import re

def get_attributes(twt):
    
    attributes = []

    first_person_pronouns = str(len(re.findall('(\/FPRP |\/FPRP$)', twt)))
    attributes.append(first_person_pronouns)
    
    second_person_pronouns = str(len(re.findall('(\/SPRP |\/SPRP$)', twt)))
    attributes.append(second_person_pronouns)
    
    thrid_person_pronouns = str(len(re.findall('(\/TPRP |\/TPRP$)', twt)))
    attributes.append(thrid_person_pronouns)
    
    coordinating_conjunctions = str(len(re.findall('(\/CC |\/CC$)', twt)))
    attributes.append(coordinating_conjunctions)
    
    past_tense_verbs = str(len(re.findall('(\/VBD |\/VBD$)', twt)))
    attributes.append(past_tense_verbs)
    
    #future_tense_verbs = #TODO: 'll, will, gonna, going+to+VB all are future tense
    
    commas = str(len(re.findall('(\/, |\/,$)', twt)))
    attributes.append(commas)
    
    colons_semicolons = str(len(re.findall('(\/: |\/:$)', twt)))
    attributes.append(colons_semicolons)
    
    dashes = str(len(re.findall('(-)', twt)))
    attributes.append(dashes)
    
    parentheses = str(len(re.findall('(\/\( |\/\($)', twt)))
    attributes.append(parentheses)
    
    #ellipses #TODO: problem is that colons_semicolons tags contain ellipses as well...
    
    
    common_singular_nouns = str(len(re.findall('(\/NN |\/NN$)', twt)))
    attributes.append(common_singular_nouns)
    
    common_plural_nouns = str(len(re.findall('(\/NNS |\/NNS$)', twt)))
    attributes.append(common_plural_nouns)
    
    proper_singular_nouns = str(len(re.findall('(\/NNP |\/NNP$)', twt)))
    attributes.append(proper_singular_nouns)
    
    proper_plural_nouns = str(len(re.findall('(\/NNPS |\/NNPS$)', twt)))
    attributes.append(proper_plural_nouns)
    
    adverb = str(len(re.findall('(\/RB |\/RB$)', twt)))
    attributes.append(adverb)
    
    adverb_comparative = str(len(re.findall('(\/RBR |\/RBR$)', twt)))
    attributes.append(adverb_comparative)
    
    adverb_superlative = str(len(re.findall('(\/RBS |\/RBS$)', twt)))
    attributes.append(adverb_superlative)
    
    
    wh_words = str(len(re.findall('(\/WDT |\/WDT$)', twt)) + len(re.findall('(\/WP|\/WP$)', twt)) + len(re.findall('(\/WRB |\/WRB$)', twt)))
    attributes.append(wh_words)
    
    #modern_slang TODO: taging or check arff for modern_slang
    
    #all_uppercase_words TODO: can't just tag must do this here
    
    particle = str(len(re.findall('(\/RP |\/RP$)', twt)))
    attributes.append(particle)
    
    return attributes
    