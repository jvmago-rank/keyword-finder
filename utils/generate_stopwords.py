import nltk
from nltk.corpus import stopwords
from abc import ABC, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def generate_stopwords(self):
        pass

class English(Strategy):
    
    def generate_stopwords(self):
        downloaded = nltk.download('stopwords')
        return stopwords.words('english')

class Spanish(Strategy):

    def generate_stopwords(self):
        



