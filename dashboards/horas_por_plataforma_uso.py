import plotly.express as px

class HorasPorPlataforma:
    def __init__(self, df):
        self.df = df

    def plot(self):
        # Usar MEDIANA em vez de média
        df_agrupado = self.df.groupby('Plataforma_mais_usada')['Horas_Media_de_Uso_Diario'].median().reset_index()
        df_agrupado = df_agrupado.sort_values('Horas_Media_de_Uso_Diario', ascending=False)

        fig = px.bar(
            df_agrupado,
            x='Plataforma_mais_usada',
            y='Horas_Media_de_Uso_Diario',
            title='Uso Diário por Plataforma',
            labels={
                'Plataforma_mais_usada': 'Plataforma',
                'Horas_Media_de_Uso_Diario': 'Uso Diário'
            },
            color='Horas_Media_de_Uso_Diario',
            color_continuous_scale='oranges'
        )
        fig.update_traces(
            texttemplate='%{y:.2f}h',
            textposition='outside',
            textfont=dict(size=11, color='white')  
        )
        fig.update_layout(title_x=0.3, xaxis_tickangle=-45)
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        return fig