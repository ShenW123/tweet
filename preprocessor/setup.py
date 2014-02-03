'''
Created on 2014-01-29

@author: Shen Wang
'''
import re

def add_abbr():
    '''
    Add all abbreviations to abbreviation dictionary for easy lookup
    '''
    abbrall = {}
    abbrfile = file("Wordlists/abbrev.english", "r")
    abbr = abbrfile.readline()
    while abbr:
        abbr = re.sub('\n', '', abbr)
        abbrall[abbr] = 1;
        abbr = abbrfile.readline()
    abbrfile.close()
    return abbrall

def add_fpp():
    '''
    Adds all first person pronouns to a dictionary
    '''
    fppall = {}
    ffpfile = file("Wordlists/First-person", "r")
    ffp = ffpfile.readline()
    while ffp:
        ffp = re.sub('\n', '', ffp)
        fppall[ffp.lower()] = 1;
        ffp = ffpfile.readline()
    ffpfile.close()
    return fppall

def add_spp():
    '''
    Adds all second person pronouns to a dictionary
    '''
    sppall = {}
    sppfile = file("Wordlists/Second-person", "r")
    spp = sppfile.readline()
    while spp:
        spp = re.sub('\n', '', spp)
        sppall[spp.lower()] = 1;
        spp = sppfile.readline()
    sppfile.close()
    return sppall

def add_tpp():
    '''
    Adds all third person pronouns to a dictionary
    '''
    tppall = {}
    tppfile = file("Wordlists/Third-person", "r")
    tpp = tppfile.readline()
    while tpp:
        tpp = re.sub('\n', '', tpp)
        tppall[tpp.lower()] = 1;
        tpp = tppfile.readline()
    tppfile.close()
    return tppall