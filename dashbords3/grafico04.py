import plotly.express as px 

class DispersaoDesempregoApoio:
    def __init__(self, df3):
        self.df3 = df3

    def plot(self):
        df3 = self.df3.copy()
    
        tentativas_por_situacao = df3.groupby('situacao_urbana')['tentativas_anteriores'].sum().reset_index()

        fig_tatativas = px.pie(tentativas_por_situacao,
                    values='tentativas_anteriores',
                    names='situacao_urbana',
                    title='<b>Tentativas Anteriores por Situação Urbana</b>',
                    color='situacao_urbana',
                    color_discrete_map={'Urbana':'#CC5500', 'Rural': '#FF8C00'},
                    hole=0.3)

        fig_tatativas.update_traces(
            textposition='inside',
            textinfo='percent+label',
            textfont_size=14,
            marker=dict(line=dict(color='white', width=2)),
            hovertemplate='<b>%{label}</b><br>Tentativas: %{value}<br>Percentual: %{percent}<extra></extra>'
        )

        fig_tatativas.update_layout(
            font=dict(size=12),
            title_x=0.3,
            showlegend=False,
            annotations=[dict(text=f"Total<br>{tentativas_por_situacao['tentativas_anteriores'].sum()}",
                            x=0.5, y=0.5, font_size=16, showarrow=False)]
        )



        return fig_tatativas