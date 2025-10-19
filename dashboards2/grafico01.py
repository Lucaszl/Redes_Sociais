# import plotly.express as px
import plotly.graph_objects as go


class PanoramaAnsiedade:
    def __init__(self, df2):
        self.df2 = df2
    
    def plot(self):
        colors = ['#FF6B35', '#FF8E53', '#FFA978']
        
        # Calcular distribuição
        contagem_ansiedade = self.df2['Nivel_de_ansiedade_(1-10)'].value_counts().sort_index()
        total_pessoas = len(self.df2)
        media = self.df2['Nivel_de_ansiedade_(1-10)'].mean()
        
        fig = go.Figure()
        
        # Barras horizontais
        fig.add_trace(go.Bar(
            y=[f"Nível {nivel}" for nivel in contagem_ansiedade.index],
            x=contagem_ansiedade.values,
            orientation='h',
            marker_color=colors[0],
            opacity=0.8,
            hovertemplate="<b>%{y}</b><br>%{x} pessoas (%{customdata:.1f}%)<extra></extra>",
            customdata=(contagem_ansiedade.values / total_pessoas * 100)
        ))
        
        
        for i, (nivel, count) in enumerate(contagem_ansiedade.items()):
            porcentagem = (count / total_pessoas) * 100
            fig.add_annotation(
                x=count / 2,  
                y=i,
                text=f"{porcentagem:.1f}%",
                showarrow=False,
                font=dict(color='white', size=11, weight='bold'),
                xanchor='center'
            )
        
        
        nivel_medio_idx = list(contagem_ansiedade.index).index(int(media)) if int(media) in contagem_ansiedade.index else len(contagem_ansiedade) - 1
        
        fig.add_trace(go.Scatter(
            y=[nivel_medio_idx - 0.5, nivel_medio_idx + 0.5],
            x=[contagem_ansiedade.max() * 1.05, contagem_ansiedade.max() * 1.05],
            mode="lines+text",
            line=dict(color=colors[1], width=2),
            text=[f" Média: {media:.1f}", ""],
            textposition="middle right",
            textfont=dict(color=colors[1], size=12),
            showlegend=False,
            hoverinfo="skip"
        ))
        
        fig.update_layout(
            title=dict(
                text="<b>Como as Pessoas se Sentem?</b><br>"
                     "<sub>Distribuição dos Níveis de Ansiedade</sub>",
                x=0.5,
                xanchor="center"
            ),
            xaxis=dict(
                title="Número de Pessoas",
                showgrid=True,
                gridcolor='lightgray',
                zeroline=False
            ),
            yaxis=dict(
                title="Nível de Ansiedade",
                tickmode="array",
                tickvals=list(range(len(contagem_ansiedade))),
                ticktext=[f"Nível {nivel}" for nivel in contagem_ansiedade.index]
            ),
            showlegend=False,
            height=450,
            margin=dict(l=80, r=80, t=100, b=80),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        return fig
