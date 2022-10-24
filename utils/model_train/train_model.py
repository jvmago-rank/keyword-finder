#%%
from cmath import cos
import os
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import pandas as pd
import numpy as np
import pickle

os.chdir("../../")
from utils import text_preprocessing as tp
#%%
data = pd.read_csv('utils/model_train/df_train.csv', index_col=0)
#dados1 = np.array(['Texto 1','pt-BR',text1])
#dados2 = np.array(['Texto 2','pt-BR',text2])
#dados = pd.DataFrame(columns=['Nome do APP','Idioma','Description'], data=[dados1,dados2])

#data = data.append(dados,ignore_index=True)
#%%
tagged_data = [TaggedDocument(words=words, tags=[i]) for i, words in enumerate(data['Description'])]
model = Doc2Vec(vector_size=300,alpha=0.025, min_count=1, dm=1)
model.build_vocab(tagged_data)
model.train(tagged_data, total_examples=model.corpus_count, epochs=100)
pickle.dump(model, open('models/doc2vec_v1.sav','wb'))

#%%