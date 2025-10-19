import plotly.express as px 
import pandas as pd 

class FumoAnsiedade:
    def __init__(self, df2):
        self.df2 = df2

    def plot(self):
        media_ansiedade = self.df2.groupby('Status_de_Fumo_(S/N)')['Nivel_de_ansiedade_(1-10)'].mean()

        
        media_percent = 100 * media_ansiedade / media_ansiedade.sum()

        fig_fumo = px.pie(
            names=media_percent.index,
            values=media_percent.values,
            title='Nivel de Ansiedade por Consumo de Fumo',
            color_discrete_sequence=['#FF6B35', '#FF9F33']
        )
        # 
        fig_fumo.update_traces(
            textinfo='percent+label',
            pull=[0, 0.2],
            hovertemplate='%{label}: %{value:.2f}%<extra></extra>'
        )

        fig_fumo.update_layout(
            title_x=0.3,
            paper_bgcolor='rgba(0,0,0,0)'
        )

        return fig_fumo
