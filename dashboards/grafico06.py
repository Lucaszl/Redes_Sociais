import plotly.express as px


class RelacaoUsoSaudeMental:
    def __init__(self, df):
        self.df = df

    def plot(self):
        
        health_col = 'Pontuacao de Saude Mental' if 'Pontuacao de Saude Mental' in self.df.columns else 'Pontuacao_de_Saude_Mental'
    
       
        top_plataformas = self.df['Plataforma_mais_usada'].value_counts().nlargest(6).index
        df_filtrado = self.df[self.df['Plataforma_mais_usada'].isin(top_plataformas)].copy()
        
        print(f"\nPlataformas incluídas: {list(top_plataformas)}")
        print(f"Total de dados após filtro: {len(df_filtrado)}/{len(self.df)}")
        
        
        cores_laranja = ["#FFA500", "#FF8C00", "#FF7F50", "#FF6347", "#FF4500", "#E67E22"]
        
        fig = px.scatter(
            df_filtrado,
            x='Horas_Media_de_Uso_Diario',
            y=health_col,
            color='Plataforma_mais_usada',
            size='Pontuacao_viciado',
            title='Relação entre Tempo de Uso e Saúde Mental por Plataforma',
            labels={
                'Horas_Media_de_Uso_Diario': 'Horas de Uso Diário (h)',
                health_col: 'Pontuação de Saúde Mental',
                'Plataforma_mais_usada': 'Plataforma',
                'Pontuacao_viciado': 'Nível de Vício'
            },
            hover_data=['Desempenho_Academico_Afetado'],
            color_discrete_sequence=cores_laranja,
            opacity=0.5
        )
        
        fig.update_layout(
            title_x=0.1,
            title_font=dict(size=15),
            xaxis=dict(
                showgrid=True, 
                gridcolor='lightgray',
                range=[0, self.df['Horas_Media_de_Uso_Diario'].max() + 1]
            ),
            yaxis=dict(
                showgrid=True, 
                gridcolor='lightgray',
                range=[0, 10] 
            )
        )

        fig.add_hline(y=5, line_dash="dot", line_color="red", 
                     annotation_text="Limite Baixa Saúde Mental")
        
        return fig