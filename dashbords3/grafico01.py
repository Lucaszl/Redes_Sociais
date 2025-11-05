# import plotly.express as px
# import requests




# class MapaDepressao:
#     def __init__(self, df3):
#         self.df3 = df3

#     def plot(self):
#             df3 = self.df3.copy()

#             url_geojson = 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'
#             response = requests.get(url_geojson)
#             geojson_brasil = response.json()


#             df_estado = df3.groupby('estado')['depressao_diagnosticada'].mean().reset_index()

#             fig_mapa = px.choropleth(df_estado,
#                                     geojson=geojson_brasil,
#                                     locations='estado',
#                                     featureidkey='properties.sigla',
#                                     color='depressao_diagnosticada',
#                                     scope='south america',
#                                     color_continuous_scale='Oranges',
#                                     labels={'depressao_diagnosticada': 'Taxa de Depressão'},
#                                     title='Taxa de Depressão Diagnosticada por Estado'
#                                     )


#             fig_mapa.update_geos(
#                 fitbounds="locations",
#                 visible=False,
#                 showcountries=True,
#                 showcoastlines=True,
#                 coastlinecolor="Black"
#             )

#             fig_mapa.update_layout(
#                 coloraxis_colorbar=dict(
#                     title="Taxa",
#                     tickformat=".0%",
#                     ticks="outside"
#                 ),
#                 title_x=0.3,
#                 title_font_size=15
#             )

#             fig_mapa.update_traces(
#                 hovertemplate='<b>%{location}</b><br>Taxa de Depressão: %{z:.1%}<extra></extra>'
#             )

#             return fig_mapa

import plotly.express as px
import json
import pandas as pd

class MapaDepressao:
    def __init__(self, df3):
        self.df3 = df3

    def plot(self):
        df3 = self.df3.copy()

        # Carrega o GeoJSON local
        with open("data/br_states.json", "r", encoding="utf-8") as f:
            geojson_brasil = json.load(f)

        # Agrupa dados
        df_estado = df3.groupby('estado')['depressao_diagnosticada'].mean().reset_index()

        # Garante que a coluna de estado está em maiúsculas
        df_estado['estado'] = df_estado['estado'].str.upper()

        # Gera o mapa
        fig_mapa = px.choropleth(
            df_estado,
            geojson=geojson_brasil,
            locations='estado',
            featureidkey='properties.sigla',
            color='depressao_diagnosticada',
            color_continuous_scale='Oranges',
            title='Taxa de Depressão Diagnosticada por Estado',
            labels={'depressao_diagnosticada': 'Taxa de Depressão'}
        )

        fig_mapa.update_geos(fitbounds="locations", visible=False)
        fig_mapa.update_layout(
            coloraxis_colorbar=dict(title="Taxa"),
            title_x=0.3
        )
        return fig_mapa




# import plotly.express as px
# import requests
# import pandas as pd

# # (Mantenha seu dicionário COORDENADAS_ESTADOS aqui)
# COORDENADAS_ESTADOS = {
#     'AC': (-8.77, -70.55), 'AL': (-9.62, -36.82), 'AP': (1.41, -51.77),
#     'AM': (-3.47, -65.10), 'BA': (-13.29, -41.71), 'CE': (-5.20, -39.53),
#     'DF': (-15.83, -47.86), 'ES': (-19.19, -40.34), 'GO': (-15.98, -49.86),
#     'MA': (-5.42, -45.44), 'MT': (-12.64, -55.42), 'MS': (-20.51, -54.54),
#     'MG': (-18.10, -44.38), 'PA': (-3.79, -52.48), 'PB': (-7.28, -36.72),
#     'PR': (-24.89, -51.55), 'PE': (-8.38, -37.86), 'PI': (-6.60, -42.28),
#     'RJ': (-22.25, -42.66), 'RN': (-5.81, -36.59), 'RS': (-30.17, -53.50),
#     'RO': (-10.83, -63.34), 'RR': (1.99, -61.33), 'SC': (-27.45, -50.95),
#     'SP': (-22.19, -48.79), 'SE': (-10.57, -37.45), 'TO': (-9.46, -48.26)
# }


# class MapaDepressao:
#     def __init__(self, df3):
#         self.df3 = df3

#     def plot(self):
#             df3 = self.df3.copy()
#             df_estado = df3.groupby('estado')['depressao_diagnosticada'].mean().reset_index()

#             df_estado['lat'] = df_estado['estado'].map(lambda x: COORDENADAS_ESTADOS.get(x, (None, None))[0])
#             df_estado['lon'] = df_estado['estado'].map(lambda x: COORDENADAS_ESTADOS.get(x, (None, None))[1])
#             df_estado = df_estado.dropna(subset=['lat', 'lon'])

#             # --- CORREÇÃO AQUI ---
#             # Os parâmetros 'locations' e 'locationmode' foram removidos.
#             fig_mapa = px.scatter_geo(df_estado,
#                                     lat='lat',
#                                     lon='lon',
#                                     color='depressao_diagnosticada',
#                                     # size='depressao_diagnosticada',
#                                     hover_name='estado',
#                                     scope='south america',
#                                     color_continuous_scale='Oranges',
#                                     labels={'depressao_diagnosticada': 'Taxa de Depressão'},
#                                     title='Taxa de Depressão Diagnosticada por Estado'
#                                     )
#             # --- FIM DA CORREÇÃO ---

#             fig_mapa.update_geos(
#                 visible=False,
#                 showcountries=True,
#                 showcoastlines=True,
#                 coastlinecolor="Black",
#                 center={"lat": -14.2350, "lon": -51.9253},
#                 lataxis_range=[-34, 6],
#                 lonaxis_range=[-75, -34]
#             )

#             fig_mapa.update_layout(
#                 coloraxis_colorbar=dict(
#                     title="Taxa",
#                     tickformat=".0%",
#                     ticks="outside"
#                 ),
#                 title_x=0.3,
#                 title_font_size=15
#             )

#             fig_mapa.update_traces(
#                 hovertemplate='<b>%{hover_name}</b><br>Taxa de Depressão: %{marker.color:.1%}<extra></extra>'
#             )

#             return fig_mapa
