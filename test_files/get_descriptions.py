#%%
import os
import shutil
from google_play_scraper import app
import pandas as pd
import re
import string
#Padrão: trabalhar com o diretorio mais pai possível
os.chdir("../")
import json
#%%
with open('utils/other_apps_for_train.json', encoding='utf-8') as fh:
    apps = json.load(fh)
#%%
for category in apps.keys():
    while os.path.exists(f'test_files/{category}'):
        shutil.rmtree(f'test_files/{category}')
    
    for appl in apps[category]:
        try:
            result = app(
                appl,
                lang='pt',
                country='br'
            )
            title = str(result['title']).translate(str.maketrans('', '', string.punctuation))
            dirr = f"test_files/{title}"
            
            with open(f"{dirr}.txt", "w+", encoding="UTF-8") as f:
                f.write(result['description'])
                f.close()
        except:
            pass
        
      

            

#%%   