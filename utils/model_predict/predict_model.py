#%%

# import os
# os.chdir("../../")
from utils import text_preprocessing as tp
from gensim.models.doc2vec import Doc2Vec

class ModelPredict():
    def __init__(self, text1: str, text2: str):
        self.text1 = text1
        self.text2 = text2
        self.model = Doc2Vec.load('models/doc2vec_v1')
    
    def predict_similarity(self):
        texts = []
        texts.append(self.text1)
        texts.append(self.text2)
        texts_preprocessed = tp.Preprocessing(texts).apply_preprocess_pipeline()
        similarity = self.model.similarity_unseen_docs(texts_preprocessed[0],texts_preprocessed[1],epochs=20)
        return similarity