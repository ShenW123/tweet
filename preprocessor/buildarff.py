'''
Created on 2014-02-02

@author: Shen Wang
'''
import attributes    
    
fileName = "tweet_test"
    
tweetfile = file("Processed/" + fileName + ".twt", "r")
writefile = file("ARFF/" + fileName + ".arff", "w")

writefile.write('@relation twit_classification\n\n')#Initialize first line

attribute_list = {"first_person_pronouns":"numeric", "second_person_pronouns": "numeric", "thrid_person_pronouns": "numeric",
              "coordinating_conjunctions": "numeric", "past_tense_verbs": "numeric", "commas": "numeric", "colons_semicolons": "numeric",
              "dashes": "numeric", "parentheses": "numeric", "common_singular_nouns": "numeric", "common_plural_nouns": "numeric", "proper_singular_nouns": "numeric"
              , "proper_plural_nouns": "numeric", "adverb": "numeric", "adverb_comparative": "numeric",
              "adverb_superlative": "numeric", "wh_words": "numeric", "particle": "numeric"
               }
for key in attribute_list:
    line = "@attribute " + key +" "+ attribute_list.get(key) + "\n"
    writefile.write(line)

writefile.write("\n") #separator
writefile.write("@data\n")

twt = tweetfile.readline() #Initialize First Line
while twt:
        values = attributes.get_attributes(twt)
        writefile.write(values[0]) #Intializes first value
        del values[0] #Deletes it so doesn't affect forloop
        for index in range(len(values)):
            writefile.write(',') #comma first so the string won't end in a comma
            writefile.write(values[index])
        writefile.write('\n') #newline at end of each
        twt = tweetfile.readline() #Read next tweet
        
writefile.write('\n') #newline at end of file?
tweetfile.close()
writefile.close()
    
    

    
    
    
    