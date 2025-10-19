import plotly.express as px 


class UsoAlcool: 
    def __init__(self, df3):
        self.df3 = df3

    def plot(self):
        df3 = self.df3.copy()
       
        uso_alcool_tabaco = df3.groupby('depressao_diagnosticada').agg({
            'uso_alcool': 'mean',
            'uso_tabaco': 'mean'
        }).reset_index()

        uso_alcool_tabaco = uso_alcool_tabaco.melt(id_vars='depressao_diagnosticada',
                                                var_name='substancia',
                                                value_name='proporcao')

        fig = px.bar(uso_alcool_tabaco,
                    x='depressao_diagnosticada',
                    y='proporcao',
                    color='substancia',
                    barmode='group',
                    title='Uso de Álcool e Tabaco por Diagnóstico de Depressão',
                    labels={
                        'depressao_diagnosticada': 'Diagnóstico de Depressão',
                        'proporcao': 'Proporção de Uso',
                        'substancia': 'Substância'
                    },
                    color_discrete_map={
                        'uso_alcool': '#712100',
                        'uso_tabaco': '#D86B32'
                    }
                    )

        fig.update_layout(yaxis_tickformat='.0%')


        fig.update_xaxes(
            ticktext=['Sem Depressão', 'Com Depressão'],
            tickvals=[0, 1]
        )

        
        fig.update_traces(
            texttemplate='%{y:.1%}',
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>%{fullData.name}: %{y:.1%}<extra></extra>'
        )

        return fig
