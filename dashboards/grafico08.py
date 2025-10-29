import plotly.express as px

class PlataformaPais:
    def __init__(self, df):
        self.df = df

    def plot(self):
        df_agregado = self.df.groupby('Pais').agg({
            'Pontuacao_de_Saude_Mental': 'mean',
            'Pontuacao_viciado': 'mean',
            'Horas_Media_de_Uso_Diario': 'mean',
            'ID_estudante': 'count'
        }).reset_index()
        
        df_agregado.columns = ['Pais', 'Saude_Mental', 'Vicio', 'Horas_Uso', 'Qtd_Estudantes']

        
        fig = px.choropleth(
            df_agregado,
            locations='Pais',           
            locationmode='country names', 
            color='Vicio',             
            hover_name='Pais',
            hover_data={
                'Saude_Mental': ':.2f',
                'Vicio': ':.2f',
                'Horas_Uso': ':.2f',
                'Qtd_Estudantes': True
            },
            color_continuous_scale='oranges',  
            title='Vício em Redes Sociais por País'
        )
        fig.update_layout(
            title_x=0.3  
        )
        return fig