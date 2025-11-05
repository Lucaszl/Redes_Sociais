import plotly.express as px

class ApoioTentativas():
    def __init__(self, df3):
        self.df3 = df3
    
    def plot(self):
        df3 = self.df3.copy()
        tabela_plot = df3.copy()
        tabela_plot['tentativas'] = tabela_plot['tentativas_anteriores'].map({0: 'Sem Tentativas', 1: 'Com Tentativas'})

        fig_violin = px.violin(
            tabela_plot,
            x='tentativas',
            y='apoio_familiar',
            title='Apoio Familiar é 3.8x Maior em Pessoas sem Tentativas de Suicídio',
            labels={'apoio_familiar': 'Apoio Familiar (0-10)'},
            color='tentativas',
                    color_discrete_map={
                    'Sem Tentativas': '#D86B32',
                    'Com Tentativas': '#712100'
                },
                    box=True,
                    points="all",
                     hover_data=tabela_plot.columns
                 )

        fig_violin.update_layout(
            title_x=0.2,
            title_font_size=15,
            showlegend=False,
            annotations=[
                dict(
                    x=0, y=6.1,
                    xref="x", yref="y",
                    text="Média: 6.1/10",
                    showarrow=True,
                    arrowhead=2,
                    ax=0, ay=-40
                ),
                dict(
                    x=1, y=2.3,
                    xref="x", yref="y",
                    text="Média: 2.3/10",
                    showarrow=True,
                    arrowhead=2,
                    ax=0, ay=40
                )
            ]
        )

        return fig_violin