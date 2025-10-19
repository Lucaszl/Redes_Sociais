import plotly.express as px

class GraficoGeneroUso:
    def __init__(self, df):
        self.df = df

    def plot(self):
        cores_generos = {'Masculino': '#f38630', 'Feminino': '#fa6900'}
        fig = px.box(
            self.df,
            x='Genero',
            y='Horas_Media_de_Uso_Diario',
            points='all',
            title='Distribuição do tempo diário de uso por gênero',
            color='Genero',
            labels={
                'Horas_Media_de_Uso_Diario': 'Tempo de Uso por Dia',
            },
            color_discrete_map=cores_generos
        )
        fig.update_layout(
            title_x=0.2, 
            title_font=dict(size=15)

        )
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        
        return fig
