#%%
import os
from google_play_scraper import app
import pandas as pd
import re
#Padrão: trabalhar com o diretorio mais pai possível
os.chdir("../../")
from utils import text_preprocessing as tp
import json
#%%
df = pd.read_excel('utils/model_train/Implementação - Planilhas Automatizadas V22 - Mobile Intelligence.xlsx',header=1)
with open('utils/other_apps.json', encoding='utf-8') as fh:
    other_apps = json.load(fh)
#%%
df = df.replace('pr-BR','pt-BR')
df = df[df['Idioma']=='pt-BR']
#%%
df = df.loc[:,['Nome do APP','Idioma','App ID']]
apps = list(df['App ID'].values)
for key in other_apps.keys():
    for appl in other_apps[key]:
        apps.append(appl)
#%%
df_texts = pd.DataFrame(columns=['App ID','Description'])
app_texts = []
app_apps_id = []
for appl in apps:
    try:
        result = app(
            appl,
            lang='pt',
            country='br'
        )
    except:
        continue
    
    app_texts.append(result['description'])
    app_apps_id.append(appl)


df_texts['App ID'] = app_apps_id
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