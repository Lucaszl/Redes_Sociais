import streamlit as st

from dashboards2.grafico01 import PanoramaAnsiedade
from dashboards2.grafico02 import NivelEstress
from dashboards2.grafico03 import Terapia
from dashboards2.grafico04 import HoraSono
from dashboards2.grafico05 import FumoAnsiedade
from dashboards2.grafico06 import MedicamentoPorAnsiedade
class Tab2:
    def __init__(self, df2):
        self.df2 = df2
        self.df_filtrado = df2.copy()
    
    def _render_filters(self):
        st.sidebar.markdown("---")
        st.sidebar.markdown("Filtros - Análise de Ansiedade")
        
        # Filtro de Idade
        idade_min = int(self.df2['Idade'].min())
        idade_max = int(self.df2['Idade'].max())
        faixa_idade = st.sidebar.slider(
            "Faixa etária", 
            idade_min, 
            idade_max,
            (idade_min, idade_max), 
            key="tab2_idade"
        )
        
        # Filtro de Gênero
        genero = st.sidebar.multiselect(
            "Gênero", 
            self.df2['Genero'].unique(),
            default=list(self.df2['Genero'].unique()),
            key="tab2_genero"
        )
        
        # Filtro de Profissão
        profissao = st.sidebar.multiselect(
            "Profissão/Cargo",
            self.df2['Profissao_Cargo'].unique(),
            default=list(self.df2['Profissao_Cargo'].unique()),
            key="tab2_profissao"
        )
        
        # Filtro de Horas de Sono
        sono_min = float(self.df2['Horas_de_Sono'].min())
        sono_max = float(self.df2['Horas_de_Sono'].max())
        horas_sono = st.sidebar.slider(
            "Horas de Sono",
            sono_min,
            sono_max,
            (sono_min, sono_max),
            key="tab2_sono"
        )
        
        # Filtro de Atividade Física
        atividade_min = float(self.df2['Atividade_Fisica_(hrs/semana)'].min())
        atividade_max = float(self.df2['Atividade_Fisica_(hrs/semana)'].max())
        atividade_fisica = st.sidebar.slider(
            "Atividade Física (horas/semana)",
            atividade_min,
            atividade_max,
            (atividade_min, atividade_max),
            key="tab2_atividade"
        )
        
        # Filtro de Cafeína
        cafeina_min = float(self.df2['Ingestao_de_Cafeina_(Por_Dia/Mg)'].min())
        cafeina_max = float(self.df2['Ingestao_de_Cafeina_(Por_Dia/Mg)'].max())
        ingestao_cafeina = st.sidebar.slider(
            "Ingestão de Cafeína (mg/dia)",
            cafeina_min,
            cafeina_max,
            (cafeina_min, cafeina_max),
            key="tab2_cafeina"
        )
        
        # Filtros de checkboxes para condições
        col1, col2 = st.sidebar.columns(2)
        with col1:
            historico_familiar = st.checkbox('Histórico Familiar', value=True, key="tab2_historico")
            medicamento = st.checkbox('Usa Medicamento', value=True, key="tab2_medicamento")
        with col2:
            terapia = st.checkbox('Faz Terapia', value=True, key="tab2_terapia")
            evento_recente = st.checkbox('Evento Recente', value=True, key="tab2_evento")
        
        # Botão de redefinir (você pode ajustar depois)
        if st.sidebar.button("Redefinir Filtros", key="tab2_redefinir"):
            for key in list(st.session_state.keys()):
                if key.startswith("tab2_"):
                    del st.session_state[key]
            st.rerun()
        
        return (faixa_idade, genero, profissao, horas_sono, 
                atividade_fisica, ingestao_cafeina, historico_familiar,
                medicamento, terapia, evento_recente)
    
    def _aplicar_filtros(self, filtros):
        (faixa_idade, genero, profissao, horas_sono, 
         atividade_fisica, ingestao_cafeina, historico_familiar,
         medicamento, terapia, evento_recente) = filtros
        
        df_filtrado = self.df2.copy()
        
        # Aplicar filtros um por um
        if genero:
            df_filtrado = df_filtrado[df_filtrado['Genero'].isin(genero)]
        
        if profissao:
            df_filtrado = df_filtrado[df_filtrado['Profissao_Cargo'].isin(profissao)]
        
        # Filtros de range
        df_filtrado = df_filtrado[
            (df_filtrado['Idade'].between(faixa_idade[0], faixa_idade[1])) &
            (df_filtrado['Horas_de_Sono'].between(horas_sono[0], horas_sono[1])) &
            (df_filtrado['Atividade_Fisica_(hrs/semana)'].between(atividade_fisica[0], atividade_fisica[1])) &
            (df_filtrado['Ingestao_de_Cafeina_(Por_Dia/Mg)'].between(ingestao_cafeina[0], ingestao_cafeina[1]))
        ]
        
        # Filtros de checkbox
        if not historico_familiar:
            df_filtrado = df_filtrado[df_filtrado['Historico_de_Ansiedade_Familiar'] == 'Nao']
        
        if not medicamento:
            df_filtrado = df_filtrado[df_filtrado['Medicamento'] == 'Nao']
        
        if not terapia:
            df_filtrado = df_filtrado[df_filtrado['Sessoes_de_terapia_(por_mes)'] == 0]
        
        if not evento_recente:
            df_filtrado = df_filtrado[df_filtrado['Evento_importante_da_vida_recente'] == 'Nao']
        
        return df_filtrado
    
    def _render_graficos(self, df_filtrado):
        if df_filtrado.empty:
            st.warning("Nenhum dado encontrado com os filtros selecionados.")
            return

        # --- Métricas gerais ---
        st.subheader('Análise de Ansiedade - GLOBAL')

        col0, col1, col2, col3, col4 = st.columns(5)
        with col0:
            total_pessoas = len(df_filtrado)
            st.metric("Total de Pessoas", f"{total_pessoas}")
        with col1:
            media_ansiedade = df_filtrado['Nivel_de_ansiedade_(1-10)'].mean()
            st.metric("Nível médio de ansiedade", f"{media_ansiedade:.2f}")

        with col2:
            media_estresse = df_filtrado['Nivel_de_Estresse_(1-10)'].mean()
            st.metric("Nível médio de estresse", f"{media_estresse:.2f}")

        with col3:
            media_sono = df_filtrado['Horas_de_Sono'].mean()
            st.metric("Média de horas de sono", f"{media_sono:.1f}")

        with col4:
            media_atividade_fisica = df_filtrado['Atividade_Fisica_(hrs/semana)'].mean()
            st.metric("Atividade física semanal", f"{media_atividade_fisica:.1f}h")

        st.divider()

        # --- Gráficos principais ---
        col1  = st.columns(1)

        with col1[0]:
            mapa_correlacao = PanoramaAnsiedade(df_filtrado)
            fig_corr = mapa_correlacao.plot()
            st.plotly_chart(fig_corr,width="stretch")

        st.divider()
       
        # col1, col2 = st.columns(2)

        col2, col3 = st.columns(2)
        with col2:
            nivel_es = NivelEstress(df_filtrado)
            nivel_estress = nivel_es.plot()
            st.plotly_chart(nivel_estress, width="stretch" )
            st.markdown("""
                **Análise:**  
                    Quanto maior o estresse, maior a ansiedade. As sessões de terapia ajudam a equilibrar esse quadro,
                    mostrando seu papel importante no bem-estar emocional.
            """)

            
        with col3:
            terapia = Terapia(df_filtrado)
            fig_terapia = terapia.plot()
            st.plotly_chart(fig_terapia, width="stretch")
            st.markdown("""
               **Análise:**                      
                Percebe-se que **quanto mais sessões de terapia**, **menor é o nível de ansiedade**.  
                Isso mostra como o acompanhamento psicológico regular contribui para o bem-estar emocional e o 
                controle do estresse.
                """)


        st.divider()
        col5, col6 = st.columns(2)
        with col5:
            medicamento = MedicamentoPorAnsiedade(df_filtrado)
            fig = medicamento.plot()
            st.plotly_chart(fig, width='streatch')
            st.markdown(
            """
            **Análise:**
            **Diferença significativa (p = 0.0000)**  

            Pessoas que **usam medicamentos** apresentam, em média, níveis de ansiedade mais
            altos do que as que não usam.

            """)
 
        with col6:
            ansiedade_fumo = FumoAnsiedade(df_filtrado)
            fig_fumo = ansiedade_fumo.plot()
            st.plotly_chart(fig_fumo, width='stretch')
            st.markdown(
            """
            **Análise:**
            Pessoas que **fumam** apresentam níveis de **ansiedade mais altos** em comparação
            com quem **não fuma**, indicando uma possível ligação entre o tabagismo e o aumento da ansiedade.
            """)
        
             
        st.divider()
        col7 = st.columns(1)
        with col7[0]:
            sono = HoraSono(df_filtrado)
            fig_horasono = sono.plot()
            st.plotly_chart(fig_horasono, width="stretch")
            st.markdown("""
                        **Análise:**
                Quem dorme menos tende a ter mais ansiedade. O gráfico reforça como o sono é essencial
                para manter a mente equilibrada.
            """)
        st.divider()
        # --- Tabela de dados filtrados ---
        st.markdown("Dados Filtrados")
        st.dataframe(df_filtrado.head(100), width="stretch")

        # Download dos dados filtrados
        csv = df_filtrado.to_csv(index=False)
        st.download_button(
            label="Download dados filtrados (CSV)",
            data=csv,
            file_name="dados_ansiedade_filtrados.csv",
            mime="text/csv"
        )
    
    def render(self):
        # Renderizar filtros
        filtros = self._render_filters()
        
        # Aplicar filtros
        df_filtrado = self._aplicar_filtros(filtros)
        
        # Renderizar gráficos
        self._render_graficos(df_filtrado)