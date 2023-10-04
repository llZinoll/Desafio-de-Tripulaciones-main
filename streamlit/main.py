import streamlit as st
from streamlit_option_menu import option_menu
import functions as ft
import os

path = os.path.dirname(__file__)
favicon = path+'/img/descarga.jpg'

st.set_page_config(page_title='EmancipaTIC', layout='wide', page_icon=favicon)



#Sidebar option 
with st.sidebar:
    selected = option_menu("EmancipaTIC", ['Home', 'Reporting','Prediction'], 
        icons=['house'], menu_icon="cast", default_index=0)
    selected

if selected == 'Home':
    ft.home()
elif selected == 'Reporting':
    ft.reporting()
elif selected == 'Prediction':
    ft.prediction()