from gensim.models import Word2Vec

class TextComparator():
    
    def __init__(self, texts):
        self.texts = texts

        self.model = Word2Vec(texts,)

    