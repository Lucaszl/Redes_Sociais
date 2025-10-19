import streamlit as st


from dashboards.grafico_conflitos import GraficoConflitosRelacionamento
from dashboards.grafico_plataforma import GraficoPlataforma
from dashboards.horas_por_plataforma_uso import HorasPorPlataforma
from dashboards.grafico_genero import GraficoGeneroUso
from dashboards.grafico_idade_horas import GraficoIdadeHoras
from dashboards.relacao_uso_saude import RelacaoUsoSaudeMental
from dashboards.impacto_sono_desempenho import ImpactoSonoDesempenho
from dashboards.plataforma_pais import PlataformaPais

class Tab1:
    def __init__(self, df):
        self.df = df
        self.df_filtrado = df.copy()
    
    def _render_filters(self):
       
        st.sidebar.markdown("---")
        
        st.sidebar.markdown("Filtros - Análise de Mídias Sociais")
        
        
        idade_min = int(self.df['Idade'].min())
        idade_max = int(self.df['Idade'].max())
        faixa_idade = st.sidebar.slider(
            'Faixa etária', 
            idade_min, 
            idade_max, 
            (idade_min, idade_max),
            key="tab1_idade"
        )
        
       
        genero = st.sidebar.multiselect(
            'Gênero',
            options=self.df['Genero'].unique(), 
            default=list(self.df['Genero'].unique()),
            key="tab1_genero"
        )
        
        
        plataforma = st.sidebar.multiselect(
            'Plataforma mais usada',
            options=self.df['Plataforma_mais_usada'].unique(),
            default=list(self.df['Plataforma_mais_usada'].unique()),
            key="tab1_plataforma"
        )
        
       
        pais = st.sidebar.multiselect(
            'País', 
            options=self.df['Pais'].unique(),
            default=list(self.df['Pais'].unique()),
            key="tab1_pais"
        )
       
        # # Redefinir filtros 
        # st.sidebar.button("Redefinir Filtros", on_click=st.session_state.clear)
        if st.sidebar.button("Redefinir Filtros"):
            for key in list(st.session_state.keys()):
                if key.startswith("tab1_"):
                    del st.session_state[key]
            st.rerun()


        return faixa_idade, genero, plataforma, pais
    
    def _aplicar_filtros(self, faixa_idade, genero, plataforma, pais):
       
        df_filtrado = self.df.copy()
        
       
        df_filtrado = df_filtrado[
            df_filtrado['Idade'].between(faixa_idade[0], faixa_idade[1])
        ]
        
       
        if genero:
            df_filtrado = df_filtrado[df_filtrado['Genero'].isin(genero)]
        
        
        if plataforma:
            df_filtrado = df_filtrado[
                df_filtrado['Plataforma_mais_usada'].isin(plataforma)
            ]
        
       
        if pais:
            df_filtrado = df_filtrado[df_filtrado['Pais'].isin(pais)]

        return df_filtrado
        
      
    def _render_graficos(self, df_filtrado):
        if df_filtrado.empty:
            st.warning('Nenhum dado encontrado com os filtros selecionados.')
            return
        
        st.subheader('Análise de Mídias Sociais GLOBAL')
        
            
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            total_estudantes = len(df_filtrado)
            st.metric("Total de Estudantes", total_estudantes)
        
        with col2:
            media_horas_uso = df_filtrado['Horas_Media_de_Uso_Diario'].mean()
            st.metric("Média de Horas de Uso Diário", f"{media_horas_uso:.1f}h")

        with col3: 
            media_saude = df_filtrado['Pontuacao_de_Saude_Mental'].mean()
            st.metric("Pontuação Média de Saúde", f"{media_saude:.1f}/10")
                
        with col4:
            media_pontuacao_vicio = df_filtrado['Pontuacao_viciado'].mean()
            st.metric("Pontuação Média de Vício", f"{media_pontuacao_vicio:.1f}/10")

        with col5:
            taxa_desempenho_afetado = (df_filtrado['Desempenho_Academico_Afetado'] == 'Yes').mean() * 100
            st.metric("Desempenho Afetado", f"{taxa_desempenho_afetado:.1f}%")

        st.divider()
        col0, col1 = st.columns(2)
        with col0:
            grafico_conflitos = GraficoConflitosRelacionamento(df_filtrado)
            st.plotly_chart(grafico_conflitos.plot(), width="stretch")
            

        with col1:
            grafico_plataforma = GraficoPlataforma(df_filtrado)
            st.plotly_chart(grafico_plataforma.plot(), width="stretch")
            

        st.divider()
        
        
        col01 = st.columns(1)
        with col01[0]:
            horas_por_plataforma = HorasPorPlataforma(df_filtrado)
            st.plotly_chart(horas_por_plataforma.plot(), width="stretch")
            

        st.divider()
        
        col2, col3 = st.columns(2)
        with col2:
            grafico_genero = GraficoGeneroUso(df_filtrado)
            st.plotly_chart(grafico_genero.plot(), width="stretch")
            st.markdown("""
            **Análise:**  
            Este gráfico mostra a **distribuição do tempo médio diário de uso das redes sociais por gênero**.
            É possível observar que o gênero **feminino apresenta maior tempo médio de uso**, com cerca de **8,5 horas por dia**, 
            enquanto o **masculino apresenta média inferior**, demonstrando um padrão de uso mais moderado.
         """)
            
        with col3: 
            grafico_idade_horas = GraficoIdadeHoras(df_filtrado)
            st.plotly_chart(grafico_idade_horas.plot(), width="stretch")
            st.markdown("""
                **Análise:**  
                O gráfico exibe o **tempo médio de uso diário conforme a faixa etária** dos respondentes.
                Observa-se que **usuários entre 18 e 20 anos** tendem a passar mais tempo nas redes sociais, 
                enquanto o uso **diminui gradualmente com o aumento da idade**, sugerindo um comportamento mais equilibrado entre faixas mais velhas.
                """)
        
        st.divider()
        
        col4, col5 = st.columns(2)
        with col4: 
            grafico_sono_uso = RelacaoUsoSaudeMental(df_filtrado)
            st.plotly_chart(grafico_sono_uso.plot(), width="stretch")
            st.markdown("""
                **Análise:**  
                Este gráfico mostra a **relação entre o tempo de uso diário das redes sociais e a pontuação de saúde mental**, segmentada por plataforma.  
                Observa-se uma **tendência negativa**: conforme as **horas de uso aumentam**, há uma **redução na pontuação de saúde mental**, indicando possíveis impactos psicológicos do uso excessivo.  
 
                """)


        with col5:
            grafico_desempenho_academico = ImpactoSonoDesempenho(df_filtrado)
            st.plotly_chart(grafico_desempenho_academico.plot(), width="stretch")
            st.markdown("""
                **Análise:**  
                Neste gráfico, analisamos a **relação entre a quantidade média de horas de sono por noite e o impacto no desempenho acadêmico**.  
                É possível observar que os estudantes que **relataram desempenho acadêmico afetado** dormem, em média, **entre 5 e 6 horas por noite**, abaixo do **mínimo recomendado de 7 a 8 horas**.  
            """)


        
        st.divider()
        
        col6 = st.columns(1)
        with col6[0]:
            plataforma_pais = PlataformaPais(df_filtrado)
            st.plotly_chart(plataforma_pais.plot(), width="stretch")
            st.markdown("""
                **Análise:**  
                Este mapa, analisamos a  
                """)


        st.divider()
        st.markdown("Dados Filtrados")
        st.dataframe(df_filtrado.head(100), width="stretch")
        
        csv = df_filtrado.to_csv(index=False)
        st.download_button(
            label="Download dados filtrados (CSV)",
            data=csv,
            file_name="students_social_media_addiction.csv",
            mime="text/csv"
        )
    def render(self):
        
        filtros = self._render_filters()
        
        
        df_filtrado = self._aplicar_filtros(*filtros)
        
        
        self._render_graficos(df_filtrado)