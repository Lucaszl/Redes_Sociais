import plotly.express as px

class Terapia: 
    def __init__(self, df2):
        self.df2 = df2

    def plot(self):
        # df2 = df2.copy()

        fig_terapia = px.scatter(
            self.df2,
            x='Sessoes_de_terapia_(por_mes)',
            y='Nivel_de_ansiedade_(1-10)',
            trendline='lowess',
            color_discrete_sequence=['#FF6B35'],
            title="<b>Sessões de Terapia vs Nível de Ansiedade</b>",
            labels={
                'Sessoes_de_terapia_(por_mes)': 'Sessões de Terapia (por mês)',
                'Nivel_de_ansiedade_(1-10)': 'Nível de Ansiedade (1–10)'
            }
        )
        fig_terapia.update_traces(marker=dict(size=8, opacity=0.7))
        fig_terapia.update_layout(
            title_x=0.3,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        return fig_terapia

