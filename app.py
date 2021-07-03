## Péricles S. G. Marques

## bibliotecas / config / covid.py
import streamlit as st
exec(open('covid.py', encoding="iso-8859-1").read())


## Config
st.set_page_config(
     page_title='COVID-19 Dashboard',
     layout="wide",
     initial_sidebar_state="expanded",
)


## funções/variáveis personalizadas
def dados(text, number):
     st.sidebar.markdown(f'<p>{text} <b style="background-color:#2c4d56;color:#09ab3b;font-size:18px;border-radius:0.25rem;">{number}</b></p>', unsafe_allow_html=True)

def formato(n,d):
    return f'{n:_.{d}f}'.replace('.',',').replace('_','.')

vac1 = mapa_brasil(z = df_estados_24h.vaccinated_per_100_inhabitants, hovertemplate = 'Vacinados: %{z:.2f}%<extra></extra>',
                    title_text='Percentual de<br>vacinados com a 1ª dose.', colorscale="rdylgn")

vac2 = mapa_brasil(z = df_estados_24h.vaccinated_second_per_100_inhabitants, hovertemplate = 'Vacinados: %{z:.2f}%<extra></extra>',
                    title_text='Percentual de<br>vacinados com a 2ª dose.', colorscale="rdylgn")

casos24h = barra_vertical(x=df_estados_24h.state, y=df_estados_24h.newCases.sort_values(ascending=False), hovertext='',
            title = "Casos nas últimas 24h (" + str(ontem_str) + "): " + str(formato(df_estados_24h_soma.newCases, 0)), xaxis_title="Estados", yaxis_title="Nº de casos")

obitos24h = barra_vertical(x=df_estados_24h.state, y=df_estados_24h.newDeaths, hovertext='',
            title = "Óbitos nas últimas 24h (" + str(ontem_str) + "): " + str(formato(df_estados_24h_soma.newDeaths, 0)), xaxis_title="Estados", yaxis_title="Nº de óbitos")

casos_100k = mapa_brasil(z = df_estados_24h.totalCases_per_100k_inhabitants, hovertemplate = 'Casos: %{z:.0f}<extra></extra>',
            title_text="Casos por 100 mil hab.", colorscale="rdylgn_r")

obitos_100k = mapa_brasil(z = df_estados_24h.deaths_per_100k_inhabitants, hovertemplate = 'Casos: %{z:.0f}<extra></extra>',
            title_text="Óbitos por 100 mil hab.", colorscale="rdylgn_r")

casos = barra_vertical(x=df_estados_24h.state, y=df_estados_24h.totalCases.sort_values(ascending=False), hovertext='',
            title = "Casos desde o início da pandemia", xaxis_title="Estados", yaxis_title="Nº de casos")

obitos = barra_vertical(x=df_estados_24h.state, y=df_estados_24h.deaths.sort_values(ascending=False), hovertext='',
            title = "Óbitos desde o início da pandemia", xaxis_title="Estados", yaxis_title="Nº de óbitos")



def main():
    cs_sidebar()
    cs_body()

    return None

# Thanks to streamlitopedia for the following code snippet


## sidebar
def cs_sidebar():
    st.sidebar.header('COVID-19 Resumo')
    dados('Dia:', ontem_str)
    st.sidebar.markdown("""---""")
    dados('Casos nas últimas 24h:', formato(df_estados_24h_soma.newCases, 0))
    dados('Óbitos nas últimas 24h:', formato(df_estados_24h_soma.newDeaths, 0))
    st.sidebar.markdown("""---""")
    dados('Casos totais:', formato(df_estados_24h_soma.totalCases, 0))
    dados('Óbitos totais:', formato(df_estados_24h_soma.deaths, 0))
    st.sidebar.markdown("""---""")
    dados('Vacinas aplicadas:', formato(df_estados_24h_soma.vaccinated+df_estados_24h_soma.vaccinated_second, 0))
    dados('Primeira dose:', formato(df_estados_24h_soma.vaccinated, 0))
    st.sidebar.progress(df_estados_24h_soma.vaccinated/214693448)
    dados('Segunda dose:', formato(df_estados_24h_soma.vaccinated_second, 0))
    st.sidebar.progress(df_estados_24h_soma.vaccinated_second/214693448)
    st.sidebar.markdown("""---""")
    return None


## body
def cs_body():    
    
    st.title('COVID-19 Dashboard')
    st.markdown("""
    #### By: [Péricles S. G. Marques](https://www.linkedin.com/in/periclessavio/)    
    Web app feito em Python e Streamlit.    
    """)
    
    st.subheader('Base de dados')
    st.write(df_base)


    st.header('')
    st.header('Últimas 24 horas')
    st.markdown("""---""")
    col1_24h, col2_24h = st.beta_columns(2)
    col1_24h.plotly_chart(casos24h, use_container_width=True)
    col2_24h.plotly_chart(obitos24h, use_container_width=True)


    st.header('')
    st.header('Casos')
    st.markdown("""---""")
    col1_casos, col2_casos = st.beta_columns(2)
    col1_casos.subheader('Casos totais')
    col1_casos.plotly_chart(casos)
    col2_casos.subheader('Casos por 100 mil hab.')
    col2_casos.plotly_chart(casos_100k)


    st.header('')
    st.header('Óbitos')
    st.markdown("""---""")
    col1_obitos, col2_obitos = st.beta_columns(2)
    col1_obitos.subheader('Óbitos totais')
    col1_obitos.plotly_chart(obitos)
    col2_obitos.subheader('Óbitos por 100 mil hab.')
    col2_obitos.plotly_chart(obitos_100k)

    
    st.header('')
    st.header('Vacinação')
    st.markdown("""---""")
    col1_vac, col2_vac = st.beta_columns(2)    
    col1_vac.subheader('Vacinação (1ª dose)')
    col1_vac.plotly_chart(vac1, use_container_width=True)
    col2_vac.subheader('Vacinação (2ª dose)')
    col2_vac.plotly_chart(vac2, use_container_width=True)
    
    return None

# Run main()

if __name__ == '__main__':
    main()

