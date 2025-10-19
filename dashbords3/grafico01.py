import plotly.express as px
import requests
class MapaDepressao:
    def __init__(self, df3):
        self.df3 = df3

    def plot(self):
            df3 = self.df3.copy()

            url_geojson = 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'
            response = requests.get(url_geojson)
            geojson_brasil = response.json()


            df_estado = df3.groupby('estado')['depressao_diagnosticada'].mean().reset_index()

            fig_mapa = px.choropleth(df_estado,
                                    geojson=geojson_brasil,
                                    locations='estado',
                                    featureidkey='properties.sigla',
                                    color='depressao_diagnosticada',
                                    scope='south america',
                                    color_continuous_scale='Oranges',
                                    labels={'depressao_diagnosticada': 'Taxa de Depressão'},
                                    title='Taxa de Depressão Diagnosticada por Estado'
                                    )


            fig_mapa.update_geos(
                fitbounds="locations",
                visible=False,
                showcountries=True,
                showcoastlines=True,
                coastlinecolor="Black"
            )

            fig_mapa.update_layout(
                coloraxis_colorbar=dict(
                    title="Taxa",
                    tickformat=".0%",
                    ticks="outside"
                ),
                title_x=0.3,
                title_font_size=15
            )

            fig_mapa.update_traces(
                hovertemplate='<b>%{location}</b><br>Taxa de Depressão: %{z:.1%}<extra></extra>'
            )

            return fig_mapa