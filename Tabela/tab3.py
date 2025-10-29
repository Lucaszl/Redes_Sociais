import streamlit as st
import pandas as pd

from dashbords3.grafico01 import MapaDepressao
from dashbords3.grafico02 import Tentativas
from dashbords3.grafico03 import UsoAlcool
from dashbords3.grafico04 import DispersaoDesempregoApoio
from dashbords3.grafico05 import ApoioTentativas
from dashbords3.grafico004 import SaudeMentalRenda


class Tab3:
    def __init__(self, df3):
        self.df3 = df3
        self.df_filtrado = df3.copy()
    
    def _render_filters(self):
        st.sidebar.markdown("---")
        st.sidebar.markdown("Filtros - Análise de Saúde Mental")
        
        
        anos_disponiveis = sorted(self.df3['ano'].unique())
        ano = st.sidebar.multiselect(
            'Ano',
            options=anos_disponiveis,
            default=anos_disponiveis,
            key="tab3_ano"
        )
        
        
        regiao = st.sidebar.multiselect(
            'Região',
            options=self.df3['regiao'].unique(),
            default=list(self.df3['regiao'].unique()),
            key="tab3_regiao"
        )
        
        
        faixa_etaria = st.sidebar.multiselect(
            'Faixa Etária',
            options=self.df3['faixa_etaria'].unique(),
            default=list(self.df3['faixa_etaria'].unique()),
            key="tab3_faixa_etaria"
        )
        
        
        genero = st.sidebar.multiselect(
            'Gênero',
            options=self.df3['genero'].unique(),
            default=list(self.df3['genero'].unique()),
            key="tab3_genero"
        )
        
        
        escolaridade = st.sidebar.multiselect(
            'Escolaridade',
            options=self.df3['escolaridade'].unique(),
            default=list(self.df3['escolaridade'].unique()),
            key="tab3_escolaridade"
        )
        
        
        situacao_urbana = st.sidebar.multiselect(
            'Situação Urbana',
            options=self.df3['situacao_urbana'].unique(),
            default=list(self.df3['situacao_urbana'].unique()),
            key="tab3_situacao_urbana"
        )
        
        
        renda_familiar = st.sidebar.multiselect(
            'Renda Familiar',
            options=self.df3['renda_familiar'].unique(),
            default=list(self.df3['renda_familiar'].unique()),
            key="tab3_renda_familiar"
        )
        
       
        desemprego_min = float(self.df3['desemprego_familiar'].min())
        desemprego_max = float(self.df3['desemprego_familiar'].max())
        desemprego_familiar = st.sidebar.slider(
            'Desemprego Familiar (%)',
            desemprego_min,
            desemprego_max,
            (desemprego_min, desemprego_max),
            key="tab3_desemprego"
        )
    
        
        col1, col2 = st.sidebar.columns(2)
        with col1:
            depressao = st.checkbox('Com Depressão', value=True, key="tab3_depressao")
            ansiedade = st.checkbox('Com Ansiedade', value=True, key="tab3_ansiedade")
        with col2:
            alcool = st.checkbox('Uso de Álcool', value=True, key="tab3_alcool")
            tabaco = st.checkbox('Uso de Tabaco', value=True, key="tab3_tabaco")
        
        # Redefinir filtros
        if st.sidebar.button("Redefinir Filtros", key="tab3_redefinir"):
            for key in list(st.session_state.keys()):
                if key.startswith("tab3_"):
                    del st.session_state[key]

            st.rerun()
    

        return (ano, regiao, faixa_etaria, genero, escolaridade, 
                situacao_urbana, renda_familiar, desemprego_familiar,
                depressao, ansiedade, alcool, tabaco)
        
    def _aplicar_filtros(self, filtros):
        (ano, regiao, faixa_etaria, genero, escolaridade, 
         situacao_urbana, renda_familiar, desemprego_familiar,
         depressao, ansiedade, alcool, tabaco) = filtros
        
        df_filtrado = self.df3.copy()
        
       
        if ano:
            df_filtrado = df_filtrado[df_filtrado['ano'].isin(ano)]
        
        if regiao:
            df_filtrado = df_filtrado[df_filtrado['regiao'].isin(regiao)]
        
        
        if faixa_etaria:
            df_filtrado = df_filtrado[df_filtrado['faixa_etaria'].isin(faixa_etaria)]
        
        if genero:
            df_filtrado = df_filtrado[df_filtrado['genero'].isin(genero)]
        
        if escolaridade:
            df_filtrado = df_filtrado[df_filtrado['escolaridade'].isin(escolaridade)]
        
        if situacao_urbana:
            df_filtrado = df_filtrado[df_filtrado['situacao_urbana'].isin(situacao_urbana)]
        
        if renda_familiar:
            df_filtrado = df_filtrado[df_filtrado['renda_familiar'].isin(renda_familiar)]
        
        
        df_filtrado = df_filtrado[
            df_filtrado['desemprego_familiar'].between(
                desemprego_familiar[0], desemprego_familiar[1]
            )
        ]
        
        
        if not depressao:
            df_filtrado = df_filtrado[df_filtrado['depressao_diagnosticada'] == 0]
        
        if not ansiedade:
            df_filtrado = df_filtrado[df_filtrado['ansiedade_diagnosticada'] == 0]
        
        if not alcool:
            df_filtrado = df_filtrado[df_filtrado['uso_alcool'] == 0]
        
        if not tabaco:
            df_filtrado = df_filtrado[df_filtrado['uso_tabaco'] == 0]
        
        return df_filtrado
    
    def _render_graficos(self, df_filtrado):
        if df_filtrado.empty:
            st.warning('Nenhum dado encontrado com os filtros selecionados.')
            return
        
        st.subheader('Análise Saúde Mental - BRASIL')
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            total_casos = len(df_filtrado)
            st.metric("Total de Casos", total_casos)
        
        with col2:
            taxa_depressao = (df_filtrado['depressao_diagnosticada'].mean() * 100)
            st.metric("Taxa de Depressão", f"{taxa_depressao:.1f}%")
        
        with col3:
            taxa_ansiedade = (df_filtrado['ansiedade_diagnosticada'].mean() * 100)
            st.metric("Taxa de Ansiedade", f"{taxa_ansiedade:.1f}%")
        
        with col4:
            tentativas_anteriores = (df_filtrado['tentativas_anteriores'].mean() * 100)
            st.metric("Taxa de Tentativas", f"{tentativas_anteriores:.1f}%")
        with col5: 
            desemprego_familiar = df_filtrado['desemprego_familiar'].median()
            st.metric("Desemprego Familiar Médio", f"{desemprego_familiar:.1f}%")
        
        st.divider()      

        col6 = st.columns(1)
        with col6[0]:
            mapa_dep = MapaDepressao(df_filtrado)
            fig_mapa = mapa_dep.plot()
            st.plotly_chart(fig_mapa, width="stretch")
            st.markdown("""
                **Análise:**  
                Alguns estados se destacam com **maiores índices de depressão**, como **Acre (33,3%)**, **Amazonas (31,6%)**,
                **Ceará (29,5%)** e **Rondônia (29,4%)**. Esses resultados podem estar relacionados a **fatores sociais,
                econômicos** e ao **acesso limitado a serviços de saúde mental**.
                """)

        st.divider()
        
        col7, col8 = st.columns(2)

        with col7: 
            tentativas = Tentativas(df_filtrado)
            fig_tentativas = tentativas.plot()
            st.plotly_chart(fig_tentativas, width="stretch")
            st.markdown("""
            """)
        with col8:
            relacao_uso_saude = UsoAlcool(df_filtrado)
            fig_relacao = relacao_uso_saude.plot()
            st.plotly_chart(fig_relacao, width="stretch")

        st.divider()

        col9, col09 = st.columns(2)
        with col9:
            dispersao = DispersaoDesempregoApoio(df_filtrado)
            fig_dispersao = dispersao.plot()
            st.plotly_chart(fig_dispersao, width="stretch")
            st.markdown("""
                **Análise:**  
                A maioria das tentativas ocorreu em **áreas urbanas (84,2%)**, enquanto apenas **15,8%** foram registradas em zonas
                rurais, indicando maior incidência nas regiões mais populosas.
            """)

        with col09: 
            saude_mental = SaudeMentalRenda(df_filtrado)
            fig_saudemental = saude_mental.plot()
            st.plotly_chart(fig_saudemental, width="stretch")
            st.markdown("""
                **Análise:**  
                Pessoas com **menor renda familiar (0–2 salários mínimos)** apresentam **maiores índices de ansiedade,
                depressão e isolamento social**.  
                À medida que a renda aumenta, esses indicadores **tendem a diminuir**, sugerindo que fatores econômicos impactam 
                diretamente a saúde mental.
""")


        st.divider()

        col10 = st.columns(1)
        with col10[0]:
            apoio_tentativas = ApoioTentativas(df_filtrado)
            fig_apoio = apoio_tentativas.plot()
            st.plotly_chart(fig_apoio,width="stretch")
            st.markdown("""
                **Análise:**  
                O **apoio familiar médio** é de **6,1 entre pessoas sem tentativas** e apenas **2,3 entre quem já tentou**,
                mostrando que **o suporte emocional familiar é 3,8 vezes maior** em quem não apresenta histórico de tentativa 
                de suicídio.
            """)


        st.divider()
        st.write("**Dados Filtrados**")
        st.dataframe(df_filtrado.head(100), width="stretch")
        
       
        csv = df_filtrado.to_csv(index=False)
        st.download_button(
            label="Download dados filtrados (CSV)",
            data=csv,
            file_name="dados_saude_mental_filtrados.csv",
            mime="text/csv"
        )
    
    def render(self):
        
        filtros = self._render_filters()
        
        
        df_filtrado = self._aplicar_filtros(filtros)
        
        self._render_graficos(df_filtrado)