#%%
from datetime import datetime
import os
os.chdir("../../")
from utils import text_preprocessing as tp
from utils import keyword_finder as kf
from gensim.models.doc2vec import Doc2Vec
import io
from itertools import combinations
import pandas as pd
import numpy as np
import plotly.express as px
#%%
similarity_data = pd.DataFrame(columns=['Text 1','Text 2', 'Cosine Similarity'])
all_files = os.listdir('test_files/')
all_files.remove('get_descriptions.py')
model = Doc2Vec.load('models/doc2vec_v1')
now = datetime.now().strftime("%d-%m-%Y %Hi%Mi%S")
all_combinations = list(combinations(all_files,2))
for combination in all_combinations:
    text1 = io.open(f'test_files/{combination[0]}','r',encoding='utf-8').read()
    text2 = io.open(f'test_files/{combination[1]}','r',encoding='utf-8').read()
    texts = []
    texts.append(text1)
    texts.append(text2)
    texts_preprocessed = tp.Preprocessing(texts).apply_preprocess_pipeline()
    similarity = model.similarity_unseen_docs(texts_preprocessed[0],texts_preprocessed[1])
    if (similarity < 0):
        similarity = 0.0  
    new_row = np.array([combination[0],combination[1],float(similarity)])
    similarity_data.loc[len(similarity_data)] = new_row

similarity_data.to_excel(f'outputs/{now}.xlsx',sheet_name='Similaridade')
#%%
sim = pd.read_excel(f'outputs/{"03-11-2022 11i50i34"}.xlsx',sheet_name='Similaridade',index_col=0)
worsts = sim[sim['Cosine Similarity']<0.1]
worsts = worsts.sort_values(by='Cosine Similarity', ascending=False)
bests = sim[sim['Cosine Similarity']>0.6]
bests = bests.sort_values(by='Cosine Similarity', ascending=False)
# %%
fig = px.box(sim,y='Cosine Similarity')
fig.update_layout(title='<b>Boxplot dos dados de similaridade entre diferentes apps</b>', title_x=0.5,
                
                        plot_bgcolor='rgb(255,255,255)')
fig.show()
# %%
