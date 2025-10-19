import plotly.express as px


class NivelEstress: 
    def __init__(self, df2):
        self.df2 = df2 
    def plot(self):
        # df2 = df2.copy()
        nivel_estress = px.scatter(self.df2,
                        x='Nivel_de_Estresse_(1-10)',
                        y='Nivel_de_ansiedade_(1-10)',
                        trendline='lowess',
                        title='<b>Relação entre Nível de Estresse e Ansiedade</b>',
                        labels={
                            'Nivel_de_Estresse_(1-10)': 'Nível de Estresse (1-10)',
                            'Nivel_de_ansiedade_(1-10)': 'Nível de Ansiedade (1-10)'
                        })
        nivel_estress.update_traces(marker=dict(color='#FF6B35', size=8, opacity=0.7))
        nivel_estress.update_layout(plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        title_x=0.3,
                        title_font_size=16)
        return nivel_estress
