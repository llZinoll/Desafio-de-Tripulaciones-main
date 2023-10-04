import time
import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import datetime
import plotly.graph_objects as go
import os


path = os.path.dirname(__file__)
my_file = path+'/css/estilos.css'
imglogo = path+'/img/unknown.png'
imgrep = path+'/img/reportingsstock.jpg'
testr = path+'/Tablas/estrellasv.csv'
tmiemb = path+'/Tablas/miembros.csv'
tpredm = path+'/Tablas/predm.csv'
tpredv = path+'/Tablas/predv.csv'
tvol = path+'/Tablas/voluntarios.csv'


# Open css file
def opencss():
    with open(my_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



#Estructura de la pagina web
def home():
    opencss()
    c1,c2 = st.columns((1, 8))
    c1.image(imglogo, width=180, output_format="auto")
    c2.title("Red EmancipaTIC")
    st.markdown("---")
    st.subheader("Reportes disponibles en línea")
    st.markdown('Aquí podrás ver información detallada sobre los reportes de las inscripciones y valoraciones de los usuarios de Red EmancipaTIC.')
    st.image(imgrep, use_column_width='auto', output_format="auto")

def reporting():
    opencss()
    c1,c2 = st.columns((1, 8))
    c1.image(imglogo, width=180, output_format="auto")
    c2.title("Estadísticas de Red EmancipaTIC")
    st.markdown("---")
    col1, col2= st.columns((2, 5))

    #Columna de Selector
    col1.title("Gráfico")
    selector = col1.selectbox("Select",("Usuarios","Voluntarios"))
    if selector == "Usuarios":
        graph = col1.selectbox("Select",("Gráfico de barras","Gráfico de puntos"))
        inscripciones_mensuales = pd.read_csv(tmiemb)

        if graph == 'Gráfico de puntos':
            #Mascara
            dateS = str(col1.date_input('Fecha', datetime.date(2019,1,1)))[0:7]
            mask = inscripciones_mensuales['fechaInscripcion'] > dateS
            inscripciones_mensuales=inscripciones_mensuales.loc[mask]
            #Figura1
            fig = make_subplots(specs=[[{'secondary_y': True}]])

            fig.add_trace(
            go.Scatter(
            x = inscripciones_mensuales['fechaInscripcion'],
            y = inscripciones_mensuales['nPersonasInscritas'],
            name = 'Nº Personas Inscritas',
            mode = 'lines+markers',
            marker = dict(color = 'rgba(16, 112, 2, 0.8)'))
            )

            fig.update_xaxes(title_text='Meses de '+ dateS + ' a ' + time.strftime("%Y-%M"))

            fig.update_yaxes(title_text='Nº Miembros Inscritos')

            fig.update_layout(
            autosize=False,
            width=1000,
            height=500)
        
            col2.plotly_chart(fig)
        elif graph == 'Gráfico de barras':
            #Mascara
            dateS = str(col1.date_input('Fecha', datetime.date(2019,1,1)))[0:7]
            mask = inscripciones_mensuales['fechaInscripcion'] > dateS
            inscripciones_mensuales=inscripciones_mensuales.loc[mask]

            #Figura2
            fig = px.bar(inscripciones_mensuales, y='nPersonasInscritas', x='fechaInscripcion')

            fig.update_xaxes(title_text='Meses de '+ dateS + ' a ' + time.strftime("%Y-%m"))

            fig.update_yaxes(title_text='Nº Miembros Inscritos')

            fig.update_layout(
            autosize=False,
            width=1000,
            height=500)

            col2.plotly_chart(fig)
        

        
        
        
    
    if selector == "Voluntarios":
        graph = col1.selectbox("Select",("Gráfico de barras","Gráfico de puntos","Gráfico de corona"))
        inscripciones_mensuales_v = pd.read_csv(tvol)

        if graph == 'Gráfico de puntos':
            #Mascara
            dateS = str(col1.date_input('Fecha', datetime.date(2019,1,1)))[0:7]
            mask = inscripciones_mensuales_v['fechaInscripcion'] > dateS
            inscripciones_mensuales_v=inscripciones_mensuales_v.loc[mask]
            #Figura1
            fig = make_subplots(specs=[[{'secondary_y': True}]])

            fig.add_trace(
                go.Scatter(
                x = inscripciones_mensuales_v['fechaInscripcion'],
                y = inscripciones_mensuales_v['nPersonasInscritas'],
                name = 'Nº Personas Inscritas',
                mode = 'lines+markers',
                marker = dict(color = 'rgba(16, 112, 2, 0.8)'))
            )

            fig.update_layout(
                title_text='Personas Inscritas por Mes'
            )

            fig.update_xaxes(title_text='Meses de '+ dateS + ' a ' + time.strftime("%Y-%M"))

            fig.update_yaxes(title_text='Nº Voluntarios Inscritos')

            fig.update_layout(
                autosize=False,
                width=1000,
                height=500)
            #col2
            col2.plotly_chart(fig)
        elif graph == 'Gráfico de barras':
            #Mascara
            dateS = str(col1.date_input('Fecha', datetime.date(2019,1,1)))[0:7]
            mask = inscripciones_mensuales_v['fechaInscripcion'] > dateS
            inscripciones_mensuales_v=inscripciones_mensuales_v.loc[mask]

            fig = px.bar(inscripciones_mensuales_v, y='nPersonasInscritas', x='fechaInscripcion')

            fig.update_xaxes(title_text='Meses de '+ dateS + ' a ' + time.strftime("%Y-%m"))

            fig.update_yaxes(title_text='Nº Voluntarios Inscritos')

            fig.update_layout(
                autosize=False,
                width=1000,
                height=500)

            col2.plotly_chart(fig)

        elif graph == "Gráfico de corona":
            voluntarios_estrellas = pd.read_csv(testr)
            fig = px.pie(voluntarios_estrellas, values='Nº Voluntarios por Valoracion', names='estrellas', title='Nº de Voluntarios por Valoracion')
            col2.plotly_chart(fig)


    if st.button('Evolución de los registros'):
        inscripciones_mensuales_m = pd.read_csv(tmiemb)
        inscripciones_mensuales_v = pd.read_csv(tvol)

        fig = make_subplots(specs=[[{"secondary_y": False}]])

        fig.add_trace(
            go.Scatter(
            x = inscripciones_mensuales_v['fechaInscripcion'],
            y = inscripciones_mensuales_v['nPersonasInscritas'],
            name = 'Nº Personas voluntarios',
            mode = 'lines+markers',
            marker = dict(color = 'rgba(16, 112, 2, 0.8)'))
        )
        fig.add_trace(
            go.Scatter(
            x = inscripciones_mensuales_m['fechaInscripcion'],
            y = inscripciones_mensuales_m['nPersonasInscritas'],
            name = 'Nº Personas miembros',
            mode = 'lines+markers',
            marker = dict(color = 'rgba(30, 26, 255, 0.8)'))
        )

        fig.update_layout(
            title_text='Miembros y Voluntarios Inscritos por Mes'
        )

        fig.update_xaxes(title_text='Meses de 01/2019 a 12/2022')

        fig.update_yaxes(title_text='Nº Personas Inscritas')

        fig.update_layout(
                autosize=False,
                width=1000,
                height=500)

        st.plotly_chart(fig)
    


def prediction():
    c1,c2 = st.columns((1, 8))
    c1.image(imglogo, width=180, output_format="auto")
    c2.title("Forecasting registros")
    st.markdown("---")
    col1, col2= st.columns((2, 5))
    col1.title("Predicciones")
    selector = col1.selectbox("Select",("Usuarios","Voluntarios"))

    if selector == "Usuarios":
        y_test_pred2_df = pd.read_csv(tpredm)
        #Figura1
        fig = make_subplots(specs=[[{"secondary_y": False}]])

        fig.add_trace(
            go.Scatter(
            x = y_test_pred2_df['meses'],
            y = y_test_pred2_df['inscripciones'],
            name = 'Nº Miembros Inscritos Real',
            mode = 'lines+markers',
            marker = dict(color = 'rgba(16, 112, 2, 0.8)'))
        )
        fig.add_trace(
            go.Scatter(
            x = y_test_pred2_df['meses'],
            y = y_test_pred2_df['predicciones'],
            name = 'Nº Miembros Inscritos Pred',
            mode = 'lines+markers',
            marker = dict(color = 'rgba(30, 26, 255, 0.8)'))
        )

        fig.update_layout(
            title_text='Predicción últimos 4 meses de Miembros Inscritos'
        )

        fig.update_xaxes(title_text='Meses de 04/2022 a 07/2022')

        fig.update_yaxes(title_text='Nº Miembros Inscritos')

        fig.update_layout(
        autosize=False,
        width=1000,
        height=500)
        
        col2.plotly_chart(fig)
    if selector == "Voluntarios":
        y_test_pred2_df = pd.read_csv(tpredv)
        #Figura1
        fig = make_subplots(specs=[[{"secondary_y": False}]])

        fig.add_trace(
            go.Scatter(
            x = y_test_pred2_df['meses'],
            y = y_test_pred2_df['inscripciones'],
            name = 'Nº voluntarios Inscritos Real',
            mode = 'lines+markers',
            marker = dict(color = 'rgba(16, 112, 2, 0.8)'))
        )
        fig.add_trace(
            go.Scatter(
            x = y_test_pred2_df['meses'],
            y = y_test_pred2_df['predicciones'],
            name = 'Nº voluntarios Inscritos Pred',
            mode = 'lines+markers',
            marker = dict(color = 'rgba(30, 26, 255, 0.8)'))
        )

        fig.update_layout(
            title_text='Predicción últimos 4 meses de voluntarios Inscritos'
        )

        fig.update_xaxes(title_text='Meses de 04/2022 a 07/2022')

        fig.update_yaxes(title_text='Nº voluntarios Inscritos')

        fig.update_layout(
        autosize=False,
        width=1000,
        height=500)
        
        col2.plotly_chart(fig)