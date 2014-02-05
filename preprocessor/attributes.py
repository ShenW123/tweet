'''
Created on 2014-02-02

@author: Shen Wang
'''
import re

def get_number_occurances(tag, twt):
    return len(re.findall('(\/%s |\/%s$|\/%s\n)', twt))

def averageLen(lst):
    lengths = []
    for i in lst:
        lengths.append(len(i))
    return 0 if len(lengths) == 0 else (float(sum(lengths)) / len(lengths)) 

def get_attributes(twt):
    attributes = []

    first_person_pronouns = str(get_number_occurances("FPRP", twt))
    attributes.append(first_person_pronouns)
    
    second_person_pronouns = str(get_number_occurances("SPRP", twt))
    attributes.append(second_person_pronouns)
    
    thrid_person_pronouns = str(get_number_occurances("TPRP", twt))
    attributes.append(thrid_person_pronouns)
    
    coordinating_conjunctions = str(get_number_occurances("CC", twt))
    attributes.append(coordinating_conjunctions)
    
    past_tense_verbs = str(get_number_occurances("VBD", twt))
    attributes.append(past_tense_verbs)
    
    future_tense_verbs = str(len(re.findall("(going/VBG to/TO\s+\S+\/VB)|(will/MD\s+\S+\/VB)|(\'/POS+ll/NN\s+\S+\/VB)|(gonna/VBG\s+\S+\/VB)", twt, re.IGNORECASE)))
    attributes.append(future_tense_verbs)
    
    commas = str(get_number_occurances(",", twt))
    attributes.append(commas)
    
    colons_semicolons = str(len(re.findall("(:/:)|(;/:)", twt)))
    attributes.append(colons_semicolons)
    
    dashes = str(len(re.findall('(-)', twt)))
    attributes.append(dashes)
    
    parentheses = str(get_number_occurances("\(", twt))
    attributes.append(parentheses)
    
    ellipses = str(len(re.findall("(.../:)", twt)))
    attributes.append(ellipses)
    
    incorrect_ellipses = str(len(re.findall("(\W+/NN)", twt)))
    attributes.append(incorrect_ellipses)
    
    common_singular_nouns = str(get_number_occurances("NN", twt))
    attributes.append(common_singular_nouns)
    
    common_plural_nouns = str(get_number_occurances("NNS", twt))
    attributes.append(common_plural_nouns)
    
    proper_singular_nouns = str(get_number_occurances("NNP", twt))
    attributes.append(proper_singular_nouns)
    
    proper_plural_nouns = str(get_number_occurances("NNPS", twt))
    attributes.append(proper_plural_nouns)
    
    adverb = str(get_number_occurances("RB", twt))
    attributes.append(adverb)
    
    adverb_comparative = str(get_number_occurances("RBR", twt))
    attributes.append(adverb_comparative)
    
    adverb_superlative = str(get_number_occurances("RBS", twt))
    attributes.append(adverb_superlative)
    
    wh_words = str(get_number_occurances("WDT", twt) + get_number_occurances("WP", twt) + get_number_occurances("WP$", twt) + get_number_occurances("WRB", twt))
    attributes.append(wh_words)
    
    slang = str(get_number_occurances("SLANG", twt))
    attributes.append(slang)
    
    #all_uppercase_words
    allcaps_words = str(len(re.findall('(\b[A-Z]{2,}\b)(?=\/)', twt)))
    attributes.append(allcaps_words)
    
    #number of sentences
    sentences = twt.split('\n')
    del sentences[-1] #Always remove last item for it's always a NULL sentence due to splitting nature
    number_of_sentences = str(len(sentences))
    attributes.append(number_of_sentences)
    
    #average length of sentence
    alltokens = []
    for element in sentences:
        alltokens.append(element.split())
    average_length_sentence = str(averageLen(alltokens))
    attributes.append(average_length_sentence)

    #average length of tokens
    alltokens_not_punctuation = re.findall('\S+(?=\/[^.:"])', twt) 
    alltokens_not_punctuation = str(averageLen(alltokens_not_punctuation))
    attributes.append(alltokens_not_punctuation)
    
    return attributes
    