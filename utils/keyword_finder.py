import json
import pandas as pd
import numpy as np
import jellyfish
import re
import string
import unicodedata
from nltk.tokenize import word_tokenize
from collections import Counter
import nltk
import warnings
from sklearn.feature_extraction.text import CountVectorizer

from utils import strategies as st



class KeywordFinder():
    def __init__(self, long_description: str, strategy: st.Strategy = st.Portuguese()):
        self.long_description = long_description
        self.strategy = strategy
        self.stopwords = self.strategy.stopwords()

        self.len_words = len(self.long_description.split())

        self.head_tail = None
        self.short_tail = None
        self.long_tail = None

        

    def get_head_tail(self):
        try:
            co = CountVectorizer(ngram_range=(1,1),stop_words=self.stopwords)
            counts = co.fit_transform(pd.Series(self.long_description))
            headTail = pd.DataFrame(counts.sum(axis=0),columns=co.get_feature_names()).T.sort_values(0,ascending=False)
            headTail.reset_index(inplace=True)
            headTail.columns = ['Keyword', 'Count']
            headTail['Densidade'] = round(((headTail['Count'] / self.len_words)*100),2)
            headTail['Densidade'] = headTail['Densidade'].astype(str)
            headTail['Densidade'] = headTail['Densidade'] + '%'

            self.head_tail = headTail
            return self.head_tail
        
        except:
            return "Não foram encontradas head tails com o texto fornecido!"

    
    def get_short_tail(self):
        try:
            co = CountVectorizer(ngram_range=(2,2))
            counts = co.fit_transform(pd.Series(self.long_description))
            shortTail = pd.DataFrame(counts.sum(axis=0),columns=co.get_feature_names()).T.sort_values(0,ascending=False)
            shortTail.reset_index(inplace=True)
            shortTail.columns = ['Keyword', 'Count']
            shortTail['Densidade'] = round(((shortTail['Count'] / self.len_words)*100),2)
            shortTail['Densidade'] = shortTail['Densidade'].astype(str)
            shortTail['Densidade'] = shortTail['Densidade'] + '%'
            

            tmp_short = shortTail["Keyword"].str.split()
            shortTail_clean = shortTail[~(tmp_short.str[0].isin(self.stopwords) | tmp_short.str[-1].isin(self.stopwords))]

            self.short_tail = shortTail_clean
            return self.short_tail
        except:
            return "Não foram encontradas short tails com o texto fornecido!"
    
    def get_long_tail(self):
        try:
            co = CountVectorizer(ngram_range=(3,8))
            counts = co.fit_transform(pd.Series(self.long_description))
            longTail = pd.DataFrame(counts.sum(axis=0),columns=co.get_feature_names()).T.sort_values(0,ascending=False).head()
            longTail.reset_index(inplace=True)
            longTail.columns = ['Keyword', 'Count']
            longTail['Densidade'] = round(((longTail['Count'] / self.len_words)*100),2)
            longTail['Densidade'] = longTail['Densidade'].astype(str)
            longTail['Densidade'] = longTail['Densidade'] + '%'
            

            tmp_long = longTail["Keyword"].str.split()
            longTail_clean = longTail[~(tmp_long.str[0].isin(self.stopwords) | tmp_long.str[-1].isin(self.stopwords))]

            self.long_tail = longTail_clean
            return self.long_tail
        except:
            return "Não foram encontradas long tails com o texto fornecido!"

        