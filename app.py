import streamlit as st
exec(open('covid.py', encoding="latin-1").read())


# reorganizando df
df_base = df_estados_24h[["UF", "state", "Região", "newCases", "totalCases", "totalCases_per_100k_inhabitants", "newDeaths", "deaths", "deaths_per_100k_inhabitants", "deaths_by_totalCases", "tests", "tests_per_100k_inhabitants", "vaccinated", "vaccinated_per_100k_inhabitants", "vacinados_1a_dose", "vaccinated_second", "vaccinated_second_per_100k_inhabitants", "vacinados_2a_dose"]]
df_base.reset_index(drop=True, inplace=True)
df_base = df_base.rename(columns={
                            "state": "Sigla",
                            "newCases": "Novos casos",
                            "totalCases": "Total de casos",
                            "totalCases_per_100k_inhabitants": "Total de casos por 100 mil hab.",
                            "newDeaths": "Novos óbitos",
                            "deaths": "Total de óbitos",
                            "deaths_per_100k_inhabitants": "Total de óbitos por 100 mil hab.",
                            "deaths_by_totalCases": "Mortes por casos",
                            "tests": "Nº testes",
                            "tests_per_100k_inhabitants": "Testes por 100 mil hab.",
                            "vaccinated": "Vacinados (1ª dose)",
                            "vaccinated_per_100k_inhabitants": "Vacinados (1ª dose) por 100 mil hab.",
                            "vacinados_1a_dose": "% Vacinados (1ª dose)",
                            "vaccinated_second": "Vacinados (2ª dose)",
                            "vaccinated_second_per_100k_inhabitants": "Vacinados (2ª dose) por 100 mil hab.",
                            "vacinados_2a_dose": "% Vacinados (2ª dose)"})

# Initial page config

st.set_page_config(
     page_title='COVID-19 Dashboard',
     layout="centered",
     initial_sidebar_state="expanded",
)



def main():
    cs_sidebar()
    cs_body()

    return None

# Thanks to streamlitopedia for the following code snippet


# sidebar

def cs_sidebar():
    st.sidebar.header('COVID-19 Resumo')
    st.sidebar.write('Óbitos nas últimas 24h:', brasil_mortos_dia.newDeaths)
    st.sidebar.write('Óbitos totais:', brasil_mortos_dia.deaths)


    return None

##########################
# Main body of cheat sheet
##########################

def cs_body():
    # Magic commands

    st.title('COVID-19 Dashboard')
    st.markdown("""
    #### By: [Péricles S. G. Marques](https://www.linkedin.com/in/periclessavio/)    
    Web app feito em Python e Streamlit.    
    """)
    
    st.subheader('Base de dados')
    st.write(df_base)

    st.header('')
    st.header('Óbitos nas últimas 24h')
    st.plotly_chart(vbar_obitos24h, use_container_width=True)
    st.plotly_chart(br_mapa_obitos24h, use_container_width=True)

    st.header('')
    st.header('Óbitos desde o início da pandemia')
    st.plotly_chart(vbar_obitos, use_container_width=True)
    st.plotly_chart(br_mapa_obitos, use_container_width=True)

    st.header('')
    st.header('Vacinação (1ª dose)')
    st.plotly_chart(vbar_vacinados1, use_container_width=True)
    st.plotly_chart(brmapa_vacinados1, use_container_width=True)

    st.header('')
    st.header('Vacinação (2ª dose)')
    st.plotly_chart(vbar_vacinados2, use_container_width=True)
    st.plotly_chart(brmapa_vacinados2, use_container_width=True)

    

    



    return None

# Run main()

if __name__ == '__main__':
    main()