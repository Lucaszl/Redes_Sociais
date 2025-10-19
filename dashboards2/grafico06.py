import plotly.express as px
from scipy.stats import ttest_ind
# from IPython.display import display, Markdown


class MedicamentoPorAnsiedade: 
    def __init__(self, df2):
        self.df2 = df2
    def plot(self):
# --- Agrupamento e cálculo das médias ---
        media_ansiedade = self.df2.groupby('Medicamento')['Nivel_de_ansiedade_(1-10)'].mean()
        media_percent = 100 * media_ansiedade / media_ansiedade.sum()

        # --- Criar gráfico de pizza ---
        fig = px.pie(
            names=media_percent.index,
            values=media_percent.values,
            title='Nível de Ansiedade por Uso de Medicamentos',
            color_discrete_sequence=['#FF6B35', '#FF9F33']
        )

        fig.update_traces(
            textinfo='label+percent',
            pull=[0, 0.2],
            hovertemplate='%{label}: %{value:.2f}%<extra></extra>'
        )

        fig.update_layout(
            title_x=0.3,
            paper_bgcolor='rgba(0,0,0,0)'
        )

        # ---  estatístico ---
        usa = self.df2[self.df2['Medicamento'] == 'Sim']['Nivel_de_ansiedade_(1-10)']
        nao_usa = self.df2[self.df2['Medicamento'] == 'Nao']['Nivel_de_ansiedade_(1-10)']

        t_stat, p_val = ttest_ind(usa, nao_usa, equal_var=False)


        if p_val < 0.05:
            conclusao = (
                f"Diferença significativa (p = {p_val:.4f}).\n\n"
                "Pessoas que **usam medicamentos** apresentam, em média, níveis de ansiedade mais altos "
                "do que as que não usam.\n\n"
                "Isso pode indicar que o uso de medicamentos está associado a casos de ansiedade mais severa "
                "(pessoas com mais sintomas tendem a usar medicação). Além disso, efeitos psicológicos e placebo "
                "podem influenciar a percepção da melhora ou piora dos sintomas quando o medicamento acaba."
            )
        else:
            conclusao = (
                f"Sem diferença significativa (p = {p_val:.4f}).\n\n"
                "Não há evidências de diferença no nível médio de ansiedade entre pessoas que usam ou não medicamentos."
            )

        # --- Exibir gráfico e texto no Colab ---
        return fig
