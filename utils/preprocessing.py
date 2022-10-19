import string
import re
class Preprocessing():

    def __init__(self, texts):
        self.texts = texts
    
    def to_lower_texts(self):
        for i, text in enumerate(self.texts):
            self.texts[i] = text.lower()
    
    def remove_punctuation(self):
        for i, text in enumerate(self.texts):
            self.texts[i] = "".join([j for j in text if j not in string.punctuation])

    def tokenize_texts(self):
        self.texts = [substring.split() for substring in self.texts]

    def apply_preprocess_pipeline(self):
        self.to_lower_texts()
        self.remove_punctuation()
        self.tokenize_texts()
        return self.texts