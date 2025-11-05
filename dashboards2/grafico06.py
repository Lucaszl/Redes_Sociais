import plotly.express as px



class MedicamentoPorAnsiedade: 
    def __init__(self, df2):
        self.df2 = df2
    def plot(self):

        media_ansiedade = self.df2.groupby('Medicamento')['Nivel_de_ansiedade_(1-10)'].mean()
        media_percent = 100 * media_ansiedade / media_ansiedade.sum()

       
        fig = px.pie(
            names=media_percent.index,
            values=media_percent.values,
            title='Nível de Ansiedade por Uso de Medicamentos',
            color_discrete_sequence=['#FF6B35', '#FF9F33']
        )

        fig.update_traces(
            textinfo='label+percent',
            pull=[0, 0.2],
            hovertemplate='%{label}: %{value:.2f}%<extra></extra>'
        )

        fig.update_layout(
            title_x=0.3,
            paper_bgcolor='rgba(0,0,0,0)'
        )

        return fig
