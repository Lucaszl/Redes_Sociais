import plotly.express as px

class ImpactoSonoDesempenho:
    def __init__(self, df):
        self.df = df

    def plot(self):
       
        desempenho_valores = self.df['Desempenho_Academico_Afetado'].unique()
        
         
        
        df_plot = self.df.copy()
        if 'Yes' in desempenho_valores:
            df_plot['Desempenho_Label'] = df_plot['Desempenho_Academico_Afetado'].map({'Yes': 'Sim', 'No': 'Não'})
            
        else:
            df_plot['Desempenho_Label'] = df_plot['Desempenho_Academico_Afetado']
      
        
        
       
        fig = px.box(
            df_plot,
            x='Desempenho_Label',
            y='Horas_de_sono_por_noite',
            color='Desempenho_Label',
            title='Relação entre Horas de Sono e Desempenho Acadêmico',
            labels={
                'Desempenho_Label': 'Desempenho Acadêmico Afetado',
                'Horas_de_sono_por_noite': 'Horas de Sono por Noite'
            },
            color_discrete_map={'Sim': '#f38630', 'Não':  '#fa6900' , 'Yes': '#f38630', 'No': '#fa6900'}
        )
        
    
        fig.add_hline(y=5, line_dash="dash", line_color="orange", 
                     annotation_text="Mínimo recomendado: 5h")
        fig.add_hline(y=8, line_dash="dash", line_color="orange", 
                     annotation_text="Máximo recomendado: 8h")
        
        fig.update_layout(
            title_x=0.1,
            title_font=dict(size=16),
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='lightgray'),
            showlegend=False
        )
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        
        return fig