import streamlit as st
import pandas as pd
from PIL import Image
from google_play_scraper import app
from utils import keyword_finder as kf
from utils import list_strategies as ls
from utils import auto_match_language as aml
from utils.model_predict import predict_model as pm
from streamlit_option_menu import option_menu


with st.sidebar:
	selected = option_menu("Main Menu", ["Keyword Finder", 'Text Similarity'], 
        icons=['search', 'card-text'], menu_icon="cast", default_index=0)


if selected == 'Keyword Finder':
	all_strategies = ls.all_strategies

	# Título
	# Imagem
	img = Image.open('kwd_logo.png')
	st.image(img)

	st.write('''Esta aplicação tem como objetivo encontrar possíveis Keywords e sua densidade
	em textos.''')


	longa = st.text_area('Insira um texto:', value="")




	if longa != "" :
		auto_idioma = aml.auto_match_language(longa)
		print(auto_idioma)
		idioma = st.text_input(
			'Idioma do texto acima:',
			value = auto_idioma,
			disabled=True
		)
		########## Infos sobre o texto ##########
		wds = len(longa.split())
		chrt = len(longa)
		chrt_s_space = sum(len(x) for x in longa.split())

		

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



elif selected == "Text Similarity":
	text1 = st.text_area('Primeiro texto:', value="")
	text2 = st.text_area('Segundo texto:', value="")
	if st.button('Check Similarity'):
		if text1!="" and text2!="":
			similarity = pm.ModelPredict(text1,text2).predict_similarity()
			similarity = float(format(similarity,'.2f'))
			st.markdown(f"Similaridade entre os textos: {similarity*100}")
		else:
			st.markdown("Insert two valid texts, please!")