import plotly.express as px

class GraficoConflitosRelacionamento:
    def __init__(self, df):
        self.df = df

    def plot(self):

        pais_count = self.df['Pais'].value_counts().head(10).reset_index()
        pais_count.columns = ['Pais', 'Contagem']

        genero_por_pais = (
            self.df.groupby(['Pais', 'Genero'])
            .size()
            .unstack(fill_value=0)
            .reset_index()
        )

        genero_por_pais.columns.name = None

       
        df_merged = pais_count.merge(
            genero_por_pais, left_on='Pais', right_on='Pais'
        )

        hover_data = {
            'Contagem': True
        }
        
        generos = [col for col in df_merged.columns if col not in ['Pais', 'Contagem']]
        for genero in generos:
            hover_data[genero] = True

        fig = px.bar(
            df_merged.sort_values('Contagem'),
            x='Pais',
            y='Contagem',
            text='Contagem',
            labels={'Contagem': 'Quantidade de Estudantes'},
            title='Top 10 Países com Mais Estudantes',
            color_discrete_sequence=['#fa6900'],
            hover_data=hover_data
        )

        
        fig.update_traces(
            texttemplate='%{text}', 
            textposition='outside', 
            selector=dict(type='bar')
        )
        
        fig.update_layout(
            uniformtext_minsize=8, 
            uniformtext_mode='hide',  
            title_x=0.3,
            title_font=dict(size=15),
            showlegend=False,
            xaxis={'categoryorder': 'total descending'}
        )
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        return fig
