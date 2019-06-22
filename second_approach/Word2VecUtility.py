#!/usr/bin/env python

import re
import nltk

import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
from nltk.corpus import stopwords, wordnet # importa las stop words y las palabras del ingles
from nltk.stem.porter import PorterStemmer # metodo para stemming
from nltk.stem.lancaster import LancasterStemmer # metodo para stemming
from nltk.stem import WordNetLemmatizer # metodo para lematizar

class Word2VecUtility(object):

    @staticmethod
    def review_to_wordlist( review, is_metadata=False ):
        stemmer = PorterStemmer() # instancia una forma de stemming
        wordnet_lemmatizer = WordNetLemmatizer()

        stops = set(stopwords.words("english"))
    
        # Function to convert a document to a sequence of words,
        # optionally removing stop words.  Returns a list of words.
        #
        # 1. Remove HTML
        review_text = BeautifulSoup(review).get_text()
        #
        # 2. Remove non-letters
        review_text = re.sub("[^a-zA-Z]"," ", review_text)
        #
        # 3. Convert words to lower case and split them
        words = review_text.lower().split()
        #
        # 4. Optionally remove stop words (false by default)
  

        # 5. aplica lematizacion, stemming, elimina de stop words y
        # aplica reglas lógicas para reducir la cantidad de tokens
        if(is_metadata):
            words = [wordnet_lemmatizer.lemmatize(stemmer.stem(w), pos="v") for w in words if (len(w)>1) and (w not in stops) ]
        else:
            words = [wordnet_lemmatizer.lemmatize(stemmer.stem(w), pos="v") for w in words if (len(w)>1) and (w not in stops) and wordnet.synsets(w) ] 
            
        return(words)