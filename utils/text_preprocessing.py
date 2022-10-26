import string
import re
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
    
    def remove_emojis(self):
        emoj = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"\U00002500-\U00002BEF"  # chinese char
            u"\U00002702-\U000027B0"
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            u"\U0001f926-\U0001f937"
            u"\U00010000-\U0010ffff"
            u"\u2640-\u2642" 
            u"\u2600-\u2B55"
            u"\u200d"
            u"\u23cf"
            u"\u23e9"
            u"\u231a"
            u"\ufe0f"  # dingbats
            u"\u3030"
            u"\u2022"
                        "]+", re.UNICODE)
        
        for i,text in enumerate(self.texts):
            self.texts[i] = re.sub(emoj, "",text)


    def tokenize_texts(self):
        self.texts = [substring.split() for substring in self.texts]
        
    
    def identify_languages(self):
        for text in self.texts:
            self.languages.append(aml.auto_match_language(text))
        
    
    def remove_stopwords(self):
        for i, language in enumerate(self.languages):
            stopwords = all_strategies[language].stopwords()
            self.texts[i] = [word for word in self.texts[i].split() if word not in stopwords]

    def remove_numbers(self):
        for i, text in enumerate(self.texts):
            self.texts[i] = ''.join([i for i in text if not i.isdigit()])

    def apply_preprocess_pipeline(self):
        self.remove_emojis()
        self.remove_numbers()
        self.remove_punctuation()
        self.to_lower_texts()
        self.identify_languages()
        self.remove_stopwords()

        return self.texts