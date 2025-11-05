import plotly.express as px 
import pandas as pd

class SaudeMentalRenda:
    def __init__(self, df3):
        self.df3 = df3

    def plot(self):
        df3 = self.df3.copy()
        
        metricas_por_renda = df3.groupby('renda_familiar').agg({
            'ansiedade_diagnosticada': 'sum',
            'atendimento_psicologico': 'sum',
            'isolamento_social': 'sum',
            'depressao_diagnosticada': 'sum'
        }).reset_index()

        
        ordem_renda = ['0-2', '2-4', '4-6', '6+']
        metricas_por_renda['renda_familiar'] = pd.Categorical(metricas_por_renda['renda_familiar'],
                                                            categories=ordem_renda,
                                                            ordered=True)
        metricas_por_renda = metricas_por_renda.sort_values('renda_familiar')

        
        cores_laranja = ['#CC5500', '#FF8C00', '#FFA500', '#FFB74D']

        
        fig_saudemental = px.bar(metricas_por_renda,
                    x='renda_familiar',
                    y=['ansiedade_diagnosticada', 'atendimento_psicologico', 'isolamento_social', 'depressao_diagnosticada'],
                    title='Indicadores de Saúde Mental por Faixa de Renda Familiar',
                    labels={'value': 'Número de Casos',
                            'renda_familiar': 'Renda Familiar (salários mínimos)',
                            'variable': 'Indicador de Saúde'},
                    barmode='group',
                    color_discrete_sequence=cores_laranja)

        
        nomes_melhorados = {
            'ansiedade_diagnosticada': 'Ansiedade',
            'atendimento_psicologico': 'Atendimento Psicológico',
            'isolamento_social': 'Isolamento Social',
            'depressao_diagnosticada': 'Depressão'
        }

        fig_saudemental.update_layout(
            xaxis_title='Renda Familiar (salários mínimos)',
            yaxis_title='Número de Casos',
            legend_title='Indicadores de Saúde'
        )

        
        for i, trace in enumerate(fig_saudemental.data):
            nome_original = trace.name
            if nome_original in nomes_melhorados:
                trace.name = nomes_melhorados[nome_original]

            
            trace.hovertemplate = f'<b>{nomes_melhorados[nome_original]}</b><br>Renda: %{{x}}<br>Casos: %{{y}}<extra></extra>'

        return fig_saudemental
