#%%
import os
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import pandas as pd
os.chdir("../../")
from utils import text_preprocessing as tp
import get_data_for_train as gdft
#%%
data = gdft.get_data_for_train()
data.index = [x for x in range (len(data))]


#%%
tagged_data = [TaggedDocument(words=words, tags=[i]) for i, words in enumerate(data['Description'])]
#%%
instanciate_params = {
    'min_count': 2, # Ignores all words with total frequency lower than this.
    'window': 5, # The maximum distance between the current and predicted word within a sentence.
    'dm': 1, #Defines the training algorithm. If dm=1, ‘distributed memory’ (PV-DM) is used. Otherwise, distributed bag of words (PV-DBOW) is employed.
    'vector_size': 200
}
model = Doc2Vec(**instanciate_params)

model.build_vocab(tagged_data)
train_params = {
    'corpus_iterable': tagged_data,
    'total_examples' : model.corpus_count,
    'epochs': 200
}
model.train(**train_params)
model.save('models/doc2vec_v1')
#%%
for i in range(len(data)):
    print(f'Text index: {i}')
    to_compare = i
    similar_doc = model.dv.most_similar(to_compare)
    for j in range(2):
        print(f"    => {similar_doc[j]}")
    print('\n')




#%%
model.dv.most_similar(114) #Inter

# %%
