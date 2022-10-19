import streamlit as st
import pandas as pd
from PIL import Image
from google_play_scraper import app
from utils import keyword_finder as kf
from utils import list_strategies as ls

all_strategies = ls.all_strategies

# Título
# Imagem
img = Image.open('kwd_logo.png')
st.image(img)

st.write('''Esta aplicação tem como objetivo encontrar possíveis Keywords e sua densidade
 em textos.''')


longa = st.text_area('Insira um texto:', value="")

if longa != "":
	########## Infos sobre o texto ##########
	wds = len(longa.split())
	chrt = len(longa)
	chrt_s_space = sum(len(x) for x in longa.split())

	idioma = st.selectbox(
		'Idioma do texto:',
		('Português','Inglês','Espanhol','Francês','Italiano','Alemão')
	)

	values = [wds, chrt, chrt_s_space]
	index = ['Palavras','Caracteres','Caracteres s/ espaço']

	info = pd.DataFrame(values, index=index, columns=['Informações sobre o Texto'])
	st.write(info)


	st.subheader('Keywords')
	st.write('Selecione o tipo de Keywords que deseja visualizar:')


	keywordfinder = kf.KeywordFinder(
				long_description=longa,
				strategy=all_strategies[idioma]
	)
	shortTail = keywordfinder.get_short_tail()
	headTail = keywordfinder.get_head_tail()
	longTail = keywordfinder.get_long_tail()

	# Visualizar Kwds
	if st.checkbox('Head Tail'):
		st.write(headTail)
		st.write('Densidade = Keyword / Número de Palavras')


	# Visualizar Kwds
	if st.checkbox('Short Tail'):
		st.write(shortTail)
		st.write('Densidade = Keyword / Número de Palavras')


	# Visualizar Kwds
	if st.checkbox('Long Tail'):
		st.write(longTail)
		st.write('Densidade = Keyword / Número de Palavras')