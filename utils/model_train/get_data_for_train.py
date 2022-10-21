#%%
import os
from google_play_scraper import app
import pandas as pd
import re
#Padrão: trabalhar com o diretorio mais pai possível
os.chdir("../../")
from utils import text_preprocessing as tp
#%%
df = pd.read_excel('utils/model_train/Implementação - Planilhas Automatizadas V22 - Mobile Intelligence.xlsx',header=1)
#%%
df = df.replace('pr-BR','pt-BR')
df = df[df['Idioma']=='pt-BR']
#%%
df = df.loc[:,['Nome do APP','Idioma','App ID']]
#%%
df_texts = pd.DataFrame(columns=['Nome do APP','Idioma','Description'])
app_names = []
app_languages = []
app_texts = []
for index, row in df.iterrows():
    try:
        result = app(
            row['App ID'],
            lang='pt',
            country='br'
        )
    except:
        continue
    app_names.append(row['Nome do APP'])
    app_languages.append(row['Idioma'])
    
    app_texts.append(result['description'])



df_texts['Nome do APP'] = app_names
df_texts['Idioma'] = app_languages
df_texts['Description'] = app_texts
# %% Removing descriptions duplicateds
df_texts = df_texts[~df_texts['Description'].duplicated()]
#%% Treatment
df_texts['Description'] = df_texts['Description'].apply(lambda x: re.sub(r'<.*?>', '', x))
df_texts['Description'] = df_texts['Description'].apply(lambda x: re.sub(r'\r', '', x))
df_texts['Description'] = df_texts['Description'].apply(lambda x: re.sub(r'\n', '', x))
# %% Preprocessing
preprocess = tp.Preprocessing(df_texts['Description'].values)
result = preprocess.apply_preprocess_pipeline()
df_texts['Description'] = result
#%% Save
df_texts.to_csv('utils/model_train/df_train.csv')
#%%