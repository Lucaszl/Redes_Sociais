import plotly.express as px

class HoraSono: 
    def __init__(self, df2):
        self.df2 = df2

    def plot(self):
        color_sequence = [
            '#7A3E00', '#8B4500', '#A05200', '#B56500', '#CC7A00',
            '#E68A00', '#FF9900', '#FFB84D', '#FFD580', '#FFE5B4'
            ]
        horas_sono = px.box(self.df2,
                    x='Nivel_de_ansiedade_(1-10)',
                    y='Horas_de_Sono',
                    color='Nivel_de_ansiedade_(1-10)',
                    title='<b>Impacto das Horas de Sono vs Nivel Ansiedade</b>',
                    # color_discrete_sequence=['#7A3E00', '#FF8C00', '#FFD580'],
                    color_discrete_sequence=color_sequence,
                    labels={
                        'Horas_de_Sono': 'Horas de Sono (por noite)',
                        'Nivel_de_ansiedade_(1-10)': 'Nível de Ansiedade (1-10)'
                    })
        horas_sono.update_layout(plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        title_x=0.3,
                        title_font_size=16,
                        showlegend=False)
        return horas_sono

