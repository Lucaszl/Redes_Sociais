import plotly.express as px

class GraficoHorasSono:
    def __init__(self, df):
        self.df = df

    def plot(self):
        fig = px.histogram(
        
            self.df,
            x='Horas_Media_de_Uso_Diario',
            nbins=20,
            title='Horas Médias de Uso Diário de Redes Sociais',
            color_discrete_sequence=['#fa6900'],
            labels={
                    'Horas_Media_de_Uso_Diario': 'Horas de Uso Diário',
                     'count': 'Quantidade'},
            opacity=0.7
            )
        
        # fig.update_traces(marker_color='#fa6900')
                    # Adicionar linha da média
        media = self.df['Horas_Media_de_Uso_Diario'].mean()
        fig.add_vline(
                x=media,
                line_dash="dash",
                line_color="red",
                annotation_text=f'Média: {media:.2f} horas',
                annotation_position="top"
                    )

                    # # Atualizar layout
        fig.update_layout(
                title_x=0.1,
                title_font=dict(size=16),
                xaxis=dict(
                title_font=dict(size=12),
                tickfont=dict(size=11)
                        ),
                yaxis=dict(
                title_font=dict(size=12),
                tickfont=dict(size=11)
                        ),
                showlegend=False
                    )
        
        return fig