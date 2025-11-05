import plotly.express as px
import json

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
