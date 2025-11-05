import plotly.express as px

class GraficoPlataforma:
    def __init__(self, df):
        self.df = df

    def plot(self):
       
        plataforma_count = self.df['Plataforma_mais_usada'].value_counts().reset_index()
        plataforma_count.columns = ['Plataforma', 'Contagem']

       
        genero_por_plataforma = (
            self.df.groupby(['Plataforma_mais_usada', 'Genero'])
            .size()
            .unstack(fill_value=0)  
            .reset_index()
        )

        genero_por_plataforma.columns.name = None  

        df_merged = plataforma_count.merge(
            genero_por_plataforma, left_on='Plataforma', right_on='Plataforma_mais_usada'
        )

        df_merged = df_merged.drop(columns=['Plataforma_mais_usada'])

        hover_data = {
            'Contagem': True
        }

        generos = [col for col in df_merged.columns if col not in ['Plataforma', 'Contagem']]
        for genero in generos:
            hover_data[genero] = True

        fig = px.bar(
            df_merged.sort_values('Contagem', ascending=False),
            x='Plataforma',
            y='Contagem',
            text='Contagem',
            labels={'Contagem': 'Total de Usuários'},
            title='Plataformas mais utilizadas',
            color_discrete_sequence=['#fa6900'],
            hover_data=hover_data
        )

        fig.update_traces(texttemplate='%{text}', textposition='outside', selector=dict(type='bar'))
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        fig.update_layout(title_x=0.3, title_font=dict(size=15))
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        return fig
