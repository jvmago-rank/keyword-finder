#%%
from datetime import datetime
import os
os.chdir("../../")
from utils import text_preprocessing as tp
from utils import keyword_finder as kf
from gensim.models.doc2vec import Doc2Vec
import io
from itertools import combinations
# #%%

sectors = os.listdir('test_files/')
sectors.remove('get_descriptions.py')
model = Doc2Vec.load('models/doc2vec_v1')
now = datetime.now().strftime("%d-%m-%Y %Hi%Mi%S")
with open(f'outputs/{now}.txt', 'w+', encoding='utf-8') as f:
    for sector in sectors:
        f.write(f"Setor de {sector.upper()}:\n")
        files = os.listdir(f'test_files/{sector}/')
        all_combinations = list(combinations(files,2))
        for combination in all_combinations:
            text1 = io.open(f'test_files/{sector}/{combination[0]}','r',encoding='utf-8').read()
            text2 = io.open(f'test_files/{sector}/{combination[1]}','r',encoding='utf-8').read()

            texts = []
            texts.append(text1)
            texts.append(text2)
            texts_preprocessed = tp.Preprocessing(texts).apply_preprocess_pipeline()
            similarity = model.similarity_unseen_docs(texts_preprocessed[0],texts_preprocessed[1])
            f.write(f"      => Similaridade entre '{combination[0]}' e '{combination[1]}': {similarity*100}%\n")
        f.write('\n')

f.close()

#%% Keyword Finder
kf1 = kf.KeywordFinder(text1)
kf2 = kf.KeywordFinder(text2)
keywords_text1 = {}
keywords_text2 = {}

keywords_text1['head'] = kf1.get_head_tail().head(30)
keywords_text1['short'] = kf1.get_short_tail()
keywords_text1['long'] = kf1.get_long_tail()

keywords_text2['head'] = kf2.get_head_tail()
keywords_text2['short'] = kf2.get_short_tail().head(15)
keywords_text2['long'] = kf2.get_long_tail().head(5)

commom_head = []
commom_shorts = []
commom_longs = []

for keyword in keywords_text1['head']['Keyword'].values:
    if keyword in keywords_text2['head']['Keyword'].values:
        commom_head.append(keyword)

for keyword in keywords_text1['short']['Keyword'].values:
    if keyword in keywords_text2['short']['Keyword'].values:
        commom_shorts.append(keyword)

for keyword in keywords_text1['long']['Keyword'].values:
    if keyword in keywords_text2['long']['Keyword'].values:
        commom_longs.append(keyword)
#%%
try:
    percent_head = len(commom_head)/len(keywords_text1['head'])
except:
    percent_head = 0

try:
    percent_short = len(commom_shorts)/len(keywords_text1['short'])
except:
    percent_short = 0

try:
    percent_long = len(commom_longs)/len(keywords_text1['long'])
except:
    percent_long = 0

print(f"{percent_head*100}% head tails estão em ambos textos.")
print(f"{percent_short*100}% short tails estão em ambos textos.")
print(f"{percent_long*100}% long tails estão em ambos textos.")
#%%
