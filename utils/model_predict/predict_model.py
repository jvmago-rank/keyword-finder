import os
os.chdir("../../")
from utils import text_preprocessing as tp
from sklearn.metrics.pairwise import euclidean_distances
import pickle
import io
#%%
text1 = io.open('test_files/text1.txt','r',encoding='utf-8').read()

text2 = io.open('test_files/text3.txt','r',encoding='utf-8').read()
texts = []
texts.append(text1)
texts.append(text2)
preprocess = tp.Preprocessing(texts).apply_preprocess_pipeline()
#%%
model = pickle.load(open('models/doc2vec_v1.sav','rb'))
# %%
# similar_doc = model.docvecs.most_similar(101)
# print(similar_doc[0])
#%%
a = model.infer_vector(preprocess[0]).reshape(-1,1)
b = model.infer_vector(preprocess[1]).reshape(-1,1)
similarity = model.similarity_unseen_docs(preprocess[0],preprocess[1])
#%%