import plotly.express as px
import pandas as pd

class GraficoIdadeHoras:
    def __init__(self, df):
        self.df = df

    def plot(self):
        cores_generos = {'Masculino': '#f38630', 'Feminino': '#fa6900'}
        
        df_temp = self.df.copy()
        
        df_temp['Idade'] = pd.cut(df_temp['Idade'],
                                      bins=[17, 20, 23, 26],
                                      labels=['18-20', '21-23', '24-26'])
        
        fig = px.box(
            df_temp, 
            x='Idade',
            y='Horas_Media_de_Uso_Diario',
            color='Genero',
            title='Idade vs Tempo diário de uso nas redes sociais',
            labels={    
                'Idade': 'Idade dos Respondentes',
                'Horas_Media_de_Uso_Diario': 'Tempo de Uso por Dia',
                'Genero': 'Gênero'
            },
            color_discrete_map=cores_generos,
        )
        fig.update_layout(
            title_x=0.2, 
            title_font=dict(size=15)

        )
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        
        return fig
