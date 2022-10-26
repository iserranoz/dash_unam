import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title='Dashboard')


nav = st.sidebar.selectbox("Menu",['Presentación', 'Introducción', 'Tablas agrupadas', 'Gráficos'])

if nav == 'Presentación':

	
	col1 , col2 = st.columns([4,1])
	
	col1.subheader('Diplomado en Técnicas y Modelos de la Estadística para Análisis de Datos')
	col1.markdown('Alumno: Iván Serrano Zapata')
	col1.markdown('Profesor: Manuel García Minjares')
	col2.image('images/LOGO2.png',width = 180, use_column_width = False)
	col1.markdown('Esta es el dashboard requerido por el docente como segunda tarea del módulo 2 del diplomado, el cual tiene como objetivo poner en práctica los conocimientos aprendidos en cuanto a lo que refiere a esta parte del curso.')
	col1.subheader('')
	
	

	with col1.expander("Estructura del dashboard"):
	    	st.write("""
        	La estructura del dashboard se compone de las siguientes secciones:

        	1. Presentación

        	   Describiremos brevemente los datos que usamos, la fuente y el enfoque general.

        	2. Introducción

        	   Breve descripción de los retos que nos enfrentamos en la limpieza y transformación de los datos usando Python, no se revisará extensamente el código, pero dejamos las notebook por si se requiere revisarla a detalle,
        	   revisión de las variables con las que trabajaremos y preguntas de investigación.

        	3. Tablas agrupadas

        	   En esta sección revisamos algunas tablas agrupadas que nos otorgan una buena información sobre el dataset y el caso planteado y algunas métricas que aportan mucha información.

        	4. Gráficos

        	   Visaulización de amigable que nos aporta mucha información sobre los datos y la población estudiada.""")

	with col1.expander("Requerimientos del trabajo"):
	        st.image('images/reqs.png',width = 550, use_column_width = True)	


	with col1.expander("Introducción y breve descripción de los datos"):
	    	st.write("""Para la elaboración de este dasboard usamos datos sobre casos de COVID 19 que se extrajeron de la página oficial de datos abiertos del gobierno, estos fueron descargados del siguiente [link](https://datos.gob.mx/).
			Este conjunto de datos tiene información, la cual será descrita con exactitud en la siguiente sección, muy detallada de casos reportado dentro del sistema de salud mexicano, referente a este padecimiento,
	    	lo cual nos da la posibilidad de, con diferentes herramientas estadísticas, estudiar el fenomeno y obtener información de valor""")       

	
if nav == 'Introducción':

	st.subheader('Introducción')

	st.markdown('Contexto')
	st.write("""El COVID 19 es, tal vez, es la mayor enfermedad y amenaza que ha sufrido nuestra sociedad en las últimas decadas, sus repercusiones trascienden al ámbito de salud y han afectado la dinámica social en todos los aspectos, desde la economía hasta las relaciones intrafamilaires, es por eso que decidimos plantear este pequeño análisis descriptivo con los datos otorgados por el gobierno federal sobre los casos registrados en 2022""")

	with st.expander('Preguntas de investigación'):

		 st.markdown('¿Existe algún tipo de condición, tanto de salud como de otro tipo, que sea mas propensa a tener complicaciones por COVID 19?')
		 st.markdown('')
		 st.markdown('¿Cómo nos ha ido con el COVID 19 en 2022?')

	with st.expander('Limpieza y breve descripción del dataset'):

		 st.markdown('Este dataset tenía un dimensión de 40 columnas y 5,794,027 filas, en su mayor parte venía compuesto por códigos númericos por lo que tuvimos que tranformar los valores usando la información de los catálogos que se proporcionaban en el zip, y así, poder tener una mejor claridad de los datos. Dentro del repositorio de GITHUB se deja el notebook de la limpieza, para este usamos Python.')


	with st.expander('Descripción de variables'):

		 st.markdown('Descripción de variables')
		 st.table(pd.read_csv('data/variables.csv'))
		    

if nav == 'Tablas agrupadas':
	pivot_1 = pd.read_csv('data/pivot_1.csv', index_col=0)
	pivot_2 = pd.read_csv('data/pivot_2.csv', index_col=0)
	pivot_3 = pd.read_csv('data/pivot_3.csv', index_col=0)
	pivot_4 = pd.read_csv('data/pivot_4.csv', index_col=0)
	st.subheader('Tablas agrupadas')
	st.subheader('')
	st.info('Resumen de casos entre mujeres y hombres')
	st.table(pivot_1)
	col1 , col2 = st.columns([2,2])
	col1.markdown(f"Porcentaje de casos totales de hombres: {np.round(100*pivot_1.loc[pivot_1.SEXO == 'HOMBRE', 'All'].sum()/pivot_1.loc[pivot_1.SEXO == 'All', 'All'].sum(),2)}%")
	col2.markdown(f"Porcentaje de casos totales de mujeres: {np.round(100*pivot_1.loc[pivot_1.SEXO == 'MUJER', 'All'].sum()/pivot_1.loc[pivot_1.SEXO == 'All', 'All'].sum(),2)}%")

	col1.markdown(f"Un {np.round(100*pivot_1.loc[pivot_1.SEXO == 'HOMBRE', 'SI_FALLECIO'].sum()/pivot_1.loc[pivot_1.SEXO == 'HOMBRE', 'All'].sum(),2)}% de los hombres contagiados murieron")
	col2.markdown(f"Un {np.round(100*pivot_1.loc[pivot_1.SEXO == 'MUJER', 'SI_FALLECIO'].sum()/pivot_1.loc[pivot_1.SEXO == 'MUJER', 'All'].sum(),2)}% de las mujeres contagiadas murieron")
	col1.subheader('')
	col2.subheader('')

	st.info('Resumen de casos ambulatorios y hospitalizados')
	st.table(pivot_2)
	col3 , col4 = st.columns([2,2])
	col3.markdown(f"Un {np.round(100*pivot_2.loc[pivot_2.TIPO_PACIENTE=='AMBULATORIO', 'All'].sum()/pivot_2.loc[pivot_2.TIPO_PACIENTE == 'All', 'All'].sum(),2)}% de los casos fueron ambulatorios")
	col4.markdown(f"Un {np.round(100*pivot_2.loc[pivot_2.TIPO_PACIENTE=='HOSPITALIZADO', 'All'].sum()/pivot_2.loc[pivot_2.TIPO_PACIENTE == 'All', 'All'].sum(),2)}% de los casos requirieron hospitalización")

	col3.markdown(f"Un {np.round(100*pivot_2.loc[pivot_2.TIPO_PACIENTE =='AMBULATORIO', 'SI_FALLECIO'].sum()/pivot_2.loc[pivot_2.TIPO_PACIENTE =='AMBULATORIO', 'All'].sum(),2)}% de los casos ambulatorios fallecieron")
	col4.markdown(f"Un {np.round(100*pivot_2.loc[pivot_2.TIPO_PACIENTE =='HOSPITALIZADO', 'SI_FALLECIO'].sum()/pivot_2.loc[pivot_2.TIPO_PACIENTE =='HOSPITALIZADO', 'All'].sum(),2)}% de los casos hospitalizados fallecieron")
	col3.subheader('')
	col4.subheader('')

	st.info('Resumen de casos que presentaron complicaciones graves')
	st.table(pivot_3)
	col5 , col6 = st.columns([2,2])

	col6.markdown(f"Un {np.round(100*pivot_3.loc[pivot_3.INTUBADO =='SI', 'All'].sum()/pivot_3.loc[pivot_3.INTUBADO.isin(['SI', 'NO']), 'All'].sum().sum(),2)}% de los casos con complicaciones graves fueron intubados")
	col5.markdown(f"Un {np.round(100*pivot_3.loc[pivot_3.INTUBADO.isin(['SI', 'NO']), 'All'].sum().sum()/pivot_3.loc[pivot_3.INTUBADO == 'All', 'All'].sum().sum(),2)}% de los casos tuvieron complicaciones graves")

	col5.markdown(f"Un {np.round(100*pivot_3.loc[pivot_3.INTUBADO =='SI', 'SI_FALLECIO'].sum()/pivot_3.loc[pivot_3.INTUBADO.isin(['SI']), 'All'].sum().sum(),2)}% de los pacientes intubados fallecieron")
	col6.markdown('')
	
	col5.subheader('')
	col6.subheader('')

	st.info('Resumen de personas con alguna enfermedad que fallecieron')
	st.table(pivot_4)
	col5 , col6 = st.columns([2,2])


if nav == 'Gráficos':

	graph_1 = pd.read_csv('data/fig1.csv')
	graph_2 = pd.read_csv('data/fig2.csv')
	graph_3 = pd.read_csv('data/fig5.csv')
	graph_4 = pd.read_csv('data/fig6.csv')
	graph_4.set_index('FECHA_INGRESO', inplace = True)
	graph_5 = pd.read_csv('data/fig7.csv')
	graph_5.set_index('FECHA_INGRESO', inplace = True)
	
	st.subheader('Gráficos')

	fig1, ax1 = plt.subplots()
	sns.barplot(data=graph_1, x="SI_FALLECIO", y="ENTIDAD_FEDERATIVA")

	fig2, ax1 = plt.subplots()
	sns.barplot(data=graph_2, x="CONTEO DE CASOS", y="ENTIDAD_FEDERATIVA")

	fig3, ax3 = plt.subplots()
	palette_color = sns.color_palette("light:b")
	plt.pie(graph_3['Casos atendidos'], labels=graph_3['SECTOR_DESC'], colors=palette_color, autopct='%.0f%%')

	fig4, ax4 = plt.subplots()
	graph_4['Casos'].plot()

	fig5, ax5 = plt.subplots()
	graph_5['Casos'].plot(color = 'red')

	

	st.info('Comparativo de casos por entidad federativa')
	st.markdown('Número de casos confirmados por entidad federativa')
	st.pyplot(fig2)

	st.markdown('Número de casos por entidad federativa que sí fallecieron')
	st.pyplot(fig1)

	st.markdown('Aunque es claro que en ambos casos predominan bastante las entidades que conocemos tienen una alta densidad poblacional, se observa algo interesante, entidades como baja california, Veracruz, Chihuahua y Guanajuato tienen una alta incidencia en mortalidad')
	st.subheader('')
	st.info('Comparativo de edades de los pacientes')

	st.markdown('Distribución de edades de los pacientes')
	st.image('images/graph_4.png',width = 700, use_column_width = False)

	st.markdown('Boxplot de edades de personas que sí y no fallecieron')
	st.image('images/graph_3.png',width = 700, use_column_width = False)


	st.write("""
        	

        	1. Métricas de personas que sí fallecieron

        	   Media: 66.47

        	   Mediana: 69

        	   Desviación Estandar: 18.73

        	   Kurtosis: 1.42

        	   Coeficiente de asimetría: -1.06

        	2. Métricas de personas que no fallecieron

        	   Media: 37.30

        	   Mediana: 36

        	   Desviación Estandar: 1.70

        	   Kurtosis: 0.0058

        	   Coeficiente de asimetría: 0.327""")

	st.subheader('')
	st.info('Casos por Sector donde fueron atendidos')
	st.pyplot(fig3)
	st.markdown('Como se observa el 88% de los casos fueron soportados por instituciones del estado')


	st.info('Evolucion del COVID en 2022')
	st.pyplot(fig4)
	st.markdown('Como se observa, se registraron dos picos de contagios marcados en fechas que suelen ser vacacionales, pero en general el comportamiento se ve estable a la baja')

	st.pyplot(fig5)
	st.markdown('El caso de defunciones se observa consistente y similar,con ligeros picos cuando aumentan los contagios')
















