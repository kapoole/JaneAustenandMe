# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 22:56:16 2021

@author: Kenan
"""

import nltk
import random

from nltk.corpus import gutenberg

gutenberg.fileids()

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~."?"'''

caesar = [w for w in gutenberg.words('shakespeare-caesar.txt') if w not in punctuation]
hamlet = [w for w in gutenberg.words('shakespeare-hamlet.txt') if w not in punctuation]
macbeth = [w for w in gutenberg.words('shakespeare-macbeth.txt') if w not in punctuation]


emma = [w.lower() for w in gutenberg.words('austen-emma.txt') if w not in punctuation]
persuasion = [w.lower() for w in gutenberg.words('austen-persuasion.txt') if w not in punctuation]
sense = [w.lower() for w in gutenberg.words('austen-sense.txt') if w not in punctuation]

fullJane = emma + persuasion + sense

fullShake = caesar + hamlet + macbeth

len(fullShake)


shakeBigrams = list(nltk.bigrams(fullShake))
cfd = nltk.ConditionalFreqDist(shakeBigrams)

shakeTrigrams = list(nltk.trigrams(fullShake))
tricfd = nltk.ConditionalFreqDist(shakeTrigrams)

janeBigrams = list(nltk.bigrams(fullJane))
cfdJane = nltk.ConditionalFreqDist(janeBigrams)

janeTrigrams = [((fullJane[index-2], fullJane[index-1]), current) for index, current in enumerate(fullJane)]
cfdJaneTri = nltk.ConditionalFreqDist(janeTrigrams)

def generateLineFromBigram (cfdist, word, num=16):
    for i in range(num):
        print(word, end=' ')
        word = random.choice(cfdist[word].most_common(16))[0]

def generateLineFromTrigram(cfdist, given, num=16):
    for i in range(num):
        wordList = cfdist[given].most_common(16)
        if wordList:
            word = random.choice(wordList)[0]
        else:
            word = random.choice(list(cfdist))[0]
        print(word, end = ' ')
        given = (given[1], word)
        
        
        
# load json module
import json

# create json object from dictionary
json = json.dumps(janeTrigrams)

# open file for writing, "w" 
f = open("janeTrigrams.json","w")

# write json object to file
f.write(json)

# close file
f.close()
