from utils import text_preprocessing as pp
from utils import keyword_finder as kf
from utils import strategies as st
from utils import auto_match_language as aml
from google_play_scraper import app
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
import pandas as pd
#%%
text1 = "Amigo é coisa pra se guardar"
text2 = 'Amigo é coisa pra se guardar'
texts = []
texts.append(text1)
texts.append(text2)
#%%
teste = pp.Preprocessing(texts.copy())
result = teste.apply_preprocess_pipeline()
#%%

documents_df = pd.DataFrame(texts, columns=['documents'])
def most_similar(doc_id,similarity_matrix,matrix):
    print (f'Document: {documents_df.iloc[doc_id]["documents"]}')
    print ('\n')
    print ('Similar Documents:')
    if matrix=='Cosine Similarity':
        similar_ix=np.argsort(similarity_matrix[doc_id])[::-1]
    elif matrix=='Euclidean Distance':
        similar_ix=np.argsort(similarity_matrix[doc_id])
    for ix in similar_ix:
        if ix==doc_id:
            continue
        print('\n')
        print (f'Document: {documents_df.iloc[ix]["documents"]}')
        print (f'{matrix} : {similarity_matrix[doc_id][ix]}')
'''
    Cria um one hot encoding dos documentos
'''
tagged_data = [TaggedDocument(words=words, tags=[i]) for i, words in enumerate(result)]
model_d2v = Doc2Vec(vector_size=100,alpha=0.025, min_count=1)
model_d2v.build_vocab(tagged_data)


#%%
for epoch in range(100):
    model_d2v.train(tagged_data,
                total_examples=model_d2v.corpus_count,
                epochs=model_d2v.epochs)
    
document_embeddings=np.zeros((documents_df.shape[0],100))

for i in range(len(document_embeddings)):
    document_embeddings[i]=model_d2v.docvecs[i]
    
    
pairwise_similarities=cosine_similarity(document_embeddings)
pairwise_differences=euclidean_distances(document_embeddings)

most_similar(0,pairwise_similarities,'Cosine Similarity')
most_similar(0,pairwise_differences,'Euclidean Distance')
#%%