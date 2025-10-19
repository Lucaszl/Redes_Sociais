import plotly.express as px

class Tentativas(): 
    def __init__(self, df3):
        self.df3 = df3
    

    def plot(self):
        df3 = self.df3.copy()
        df_faixa = df3.groupby('faixa_etaria')['tentativas_anteriores'].mean().reset_index()


        df_faixa = df_faixa.sort_values('tentativas_anteriores', ascending=False)

        fig_barras = px.bar(df_faixa,
                            x='faixa_etaria',
                            y='tentativas_anteriores',
                            title='Proporção de Tentativas Anteriores por Faixa Etária',
                            labels={'tentativas_anteriores': 'Proporção de Tentativas', 'faixa_etaria': 'Faixa Etária'},
                            hover_data=['tentativas_anteriores'],

                            color_discrete_sequence=['#D86B32'],
                            text_auto='.1%'
                            )

        fig_barras.update_layout(
            title_x=0.2,
            title_font=dict(size=16),
            xaxis=dict(
                showgrid=False,
                categoryorder='array',
                categoryarray=df_faixa['faixa_etaria']
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='lightgray',
                tickformat='.0%'
            ),
            showlegend=False
        )

        fig_barras.update_traces(
            textposition='outside',
            hovertemplate='%{x}Proporção: %{y:.1%}'
        )

        return fig_barras

