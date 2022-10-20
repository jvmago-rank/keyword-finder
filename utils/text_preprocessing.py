import string
from utils import strategies as stg
from utils import auto_match_language as aml
from utils import list_strategies as ls

all_strategies = ls.all_strategies
class Preprocessing():
    
    def __init__(self, texts):
        '''
            self.texts = array onde cada posição contém um texto
        '''
        self.texts = texts
        self.languages = []

    def to_lower_texts(self):
        for i, text in enumerate(self.texts):
            self.texts[i] = text.lower()
        
    
    def remove_punctuation(self):
        for i, text in enumerate(self.texts):
            self.texts[i] = text.translate(str.maketrans('', '', string.punctuation))
        
    
    def tokenize_texts(self):
        self.texts = [substring.split() for substring in self.texts]
        
    
    def identify_languages(self):
        for text in self.texts:
            self.languages.append(aml.auto_match_language(text))
        
    
    def remove_stopwords(self):
        for i, language in enumerate(self.languages):
            stopwords = all_strategies[language].stopwords()
            self.texts[i] = [word for word in self.texts[i].split() if word not in stopwords]

    def apply_preprocess_pipeline(self):
        self.remove_punctuation()
        self.to_lower_texts()
        self.identify_languages()
        self.remove_stopwords()

        return self.texts