from utils import list_strategies as ls
import numpy as np

def count(string, check):
    return len([char for char in string.split() if char == check])

def auto_match_language(long_description: str):
    all_strategies = ls.all_strategies
    more_stopwords = -np.inf
    for language, obj in all_strategies.items():
        #print("Linguagem: ",language)
        stopwords = obj.stopwords()
        quantity = 0
        for stopword in stopwords:
            quantity += int(count(long_description, stopword))
        #print("     => Quantidade: ",quantity)
        if quantity > more_stopwords:
            linguagem = language
            more_stopwords = quantity
    
    return (linguagem)


