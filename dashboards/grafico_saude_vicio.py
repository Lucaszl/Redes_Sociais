import plotly.express as px

class GraficoSaudeVicio:
    def __init__(self, df):
        self.df = df

    def plot(self):
        # Definir cores
        cores_desempenho = {'Yes': "#BF9342", 'No': '#D32F2F'}

        # Criar o gráfico
        fig = px.scatter(
            self.df, 
            x='Pontuacao_viciado',
            y='Pontuacao_de_Saude_Mental', 
            color='Desempenho_Academico_Afetado',
            trendline='ols',  
            title='Relação entre Saúde Mental e Nível de Vício em Redes Sociais',
            color_discrete_map=cores_desempenho,
            labels={
                'Pontuacao_de_Saude_Mental': 'Pontuação de Saúde Mental',
                'Pontuacao_viciado': 'Pontuação de Vício em Redes Sociais',
                'Desempenho_Academico_Afetado': 'Desempenho Afetado'
            },
            opacity=0.7,
            hover_data=['Idade', 'Genero']
        )

       
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
            )
        )

        # Atualizar os marcadores
        fig.update_traces(
            marker=dict(size=8),
            selector=dict(mode='markers')
        )

        return fig