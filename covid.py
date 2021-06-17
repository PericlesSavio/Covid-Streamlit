# bibliotecas
import plotly.express as px
import pandas as pd
import pandas as pd
import plotly.graph_objects as go

# arquivos básicos
db_states = pd.read_csv("https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv")
brasil_pop = pd.read_csv('https://raw.githubusercontent.com/PericlesSavio/Python-Notebooks/main/covid/estados_pop.csv')
df_states_pop = pd.merge(db_states, brasil_pop, left_on='state',right_on='Sigla',how='outer',suffixes=('_left','_right'))
mapa_estados = 'https://raw.githubusercontent.com/PericlesSavio/Python-Notebooks/main/covid/br_states.json'

# variável ontem e hpje
import datetime
hoje = datetime.date.today()
ontem = hoje - datetime.timedelta(days=1)
ontem = str(ontem)

# data no formato dd-mm-aaaa
from datetime import datetime
ontem2 = datetime.strptime(ontem, "%Y-%m-%d")
ontem2 = ontem2.strftime("%d-%m-%Y")

# óbitos 24h
df_estados_24h = df_states_pop[(df_states_pop.date == ontem) & (df_states_pop.state != 'TOTAL')].sort_values(by=['newDeaths'], ascending=False)
brasil_mortos_dia = df_estados_24h.sum()

    

# gráfico de barras: óbitos 24h
vbar_obitos24h = go.Figure(data=[go.Bar(x=df_estados_24h.state, y=df_estados_24h.newDeaths, hovertext=df_estados_24h.state)])
vbar_obitos24h.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
vbar_obitos24h.update_layout(title = "Óbitos nas últimas 24h (" + str(ontem2) + "): " + str(brasil_mortos_dia.newDeaths) ,
    xaxis_title="Estados", yaxis_title="Nº de óbitos", hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell")
)


#mapa: óbitos 24h
br_mapa_obitos24h = go.Figure(go.Choroplethmapbox(geojson=mapa_estados, locations=df_estados_24h.state, z=df_estados_24h.newDeaths, colorscale="burgyl",
                                    zmin=0, zmax=df_estados_24h.newDeaths.max(), marker_opacity=1, marker_line_width=1,
                                    hovertemplate = df_estados_24h.UF + "<br>Óbitos: %{z}<extra></extra>"
                                    ))
br_mapa_obitos24h.update_layout(mapbox_style="carto-positron", mapbox_zoom=2.9, mapbox_center = {"lat": -15.3556, "lon": -56.0506})
br_mapa_obitos24h.update_layout(title_text='Óbitos nas últimas 24h<br>por estado', title_y=0.1, margin={"r":0,"t":0,"l":0,"b":0})
#br_mapa_obitos24h.show()

#reordenar o df
df_estados_24h = df_estados_24h.sort_values(by=['deaths'], ascending=False)

# gráfico de barras: óbitos totais
vbar_obitos = go.Figure(data=[go.Bar(x=df_estados_24h.state, y=df_estados_24h.deaths, hovertext=df_estados_24h.state)])
vbar_obitos.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
vbar_obitos.update_layout(
    title = "Óbitos desde o início da pandemia",
    xaxis_title="Estados",
    yaxis_title="Nº de óbitos",
    hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"),
    )
#vbar_obitos.show()

#mapa: óbitos 24h
br_mapa_obitos = go.Figure(go.Choroplethmapbox(geojson=mapa_estados, locations=df_estados_24h.state, z=df_estados_24h.deaths, colorscale="burgyl",
                                    zmin=0, zmax=df_estados_24h.deaths.max(), marker_opacity=1, marker_line_width=1,
                                    hovertemplate = df_estados_24h.UF + "<br>Óbitos: %{z}<extra></extra>"
                                    ))
br_mapa_obitos.update_layout(mapbox_style="carto-positron", mapbox_zoom=2.9, mapbox_center = {"lat": -15.3556, "lon": -56.0506})
br_mapa_obitos.update_layout(title_text='Óbitos desde<br>o início da pandemia', title_y=0.1, margin={"r":0,"t":0,"l":0,"b":0})

#br_mapa_obitos.show()

## VACINAÇÃO #################################################################
# vacinados 1a dose e 2a dose
df_estados_24h['vacinados_1a_dose'] = df_estados_24h.vaccinated/df_estados_24h.População*100
df_estados_24h = df_estados_24h.sort_values(by=['vacinados_1a_dose'], ascending=False)
#df_estados_24h.head()

#gráfico de barras: vacinados 1a dose
vbar_vacinados1 = go.Figure(data=[go.Bar(x=df_estados_24h.state, y=df_estados_24h.vacinados_1a_dose, hovertext=df_estados_24h.vacinados_1a_dose)])
vbar_vacinados1.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
vbar_vacinados1.update_layout({'plot_bgcolor': 'rgba(255, 255, 255, 0)', 'paper_bgcolor': 'rgba(255, 255, 255, 0)'},
    title = "Percentual de vacinados com a 1ª dose",
    xaxis_title="Estados",
    yaxis_title="Vacinados (1ª dose)",
    hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell")
)
#vbar_vacinados1.show()

# mapa vacinados 1a dose
brmapa_vacinados1 = go.Figure(go.Choroplethmapbox(geojson=mapa_estados, locations=df_estados_24h.state, z=df_estados_24h.vaccinated/df_estados_24h.População*100,
                                    colorscale="rdylgn",
                                    zmin=(df_estados_24h.vaccinated/df_estados_24h.População*100).min(),
                                    zmax=(df_estados_24h.vaccinated/df_estados_24h.População*100).max(),
                                    marker_opacity=1, marker_line_width=1,
                                    hovertemplate = df_estados_24h.UF + "<br>Vacinados: %{z:.2f}%<extra></extra>"
                                    ))

brmapa_vacinados1.update_layout({'plot_bgcolor': 'rgba(255, 255, 255, 0)', 'paper_bgcolor': 'rgba(255, 255, 255, 0)'}, mapbox_style="carto-positron",
                  mapbox_zoom=2.9, mapbox_center = {"lat": -15.3556, "lon": -56.0506},
                  title_text='Percentual de<br>vacinados com a 1ª dose',
                  title_y=0.1, margin={"r":0,"t":0,"l":0,"b":0},
                  )
#brmapa_vacinados1.show()

#vacinados 2a dose
df_estados_24h['vacinados_2a_dose'] = df_estados_24h.vaccinated_second/df_estados_24h.População*100
df_estados_24h = df_estados_24h.sort_values(by=['vacinados_2a_dose'], ascending=False)
df_estados_24h.head()

#mapa vacina 2a dose
vbar_vacinados2 = go.Figure(data=[go.Bar(x=df_estados_24h.state, y=df_estados_24h.vacinados_2a_dose, hovertext=df_estados_24h.vacinados_2a_dose)])
vbar_vacinados2.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
vbar_vacinados2.update_layout({'plot_bgcolor': 'rgba(255, 255, 255, 0)', 'paper_bgcolor': 'rgba(255, 255, 255, 0)'},
    title = "Percentual de vacinados com a 2ª dose",
    xaxis_title="Estados",
    yaxis_title="Vacinados (2ª dose).",
    hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell")
)

#vbar_vacinados2.show()

brmapa_vacinados2 = go.Figure(go.Choroplethmapbox(geojson=mapa_estados, locations=df_estados_24h.state, z=df_estados_24h.vaccinated_second/df_estados_24h.População*100,
                                    colorscale="rdylgn",
                                    marker_opacity=1, marker_line_width=1,
                                    hovertemplate = df_estados_24h.UF + "<br>Vacinados: %{z:.2f}%<extra></extra>"
                                    ))
brmapa_vacinados2.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=2.9, mapbox_center = {"lat": -15.3556, "lon": -56.0506},
                  title_text='Percentual de<br>vacinados com a 2ª dose.',
                  title_y=0.1, margin={"r":0,"t":0,"l":0,"b":0},
                  )
brmapa_vacinados2.update_layout({
        'plot_bgcolor': 'rgba(255, 255, 255, 0)',
        'paper_bgcolor': 'rgba(255, 255, 255, 0)',
    })
#brmapa_vacinados2.show()







###########
