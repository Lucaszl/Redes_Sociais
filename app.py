import streamlit as st
import pandas as pd

from tabela.tab1 import Tab1
from tabela.tab2 import Tab2  
from tabela.tab3 import Tab3  
from tabela.tab4 import Tab4


st.set_page_config(
    page_title="Vicios em Mídias - Dashboard", 
    layout="wide",
    # page_icon="" Imagem em PNG - Neuros aqui depois
)


st.markdown("""
    <div style="background-color:#f0f2f6; padding:16px; border-radius:8px;">
        <h1 style="text-align:center; color:#FF8000; margin:0;">Vício em Mídias Sociais e seus efeitos na vida</h1>
        <h3 style="text-align:center; color:gray; margin:0;">Pessoal e Acadêmica</h3>
""", unsafe_allow_html=True)

@st.cache_data
def load_data(path):
    df = pd.read_csv(path, encoding="latin-1")
    df = df.drop(columns=[col for col in df.columns if "Unnamed" in col])
    df.columns = df.columns.str.strip().str.replace(" ", "_")
    return df

df = load_data("data/students_social_media_addiction.csv")
df2 = load_data("data/enhanced_anxiety_dataset.csv")
df3 = load_data("data/dataset_saude_mental_1500.csv")

st.sidebar.title("Navegação:")
st.sidebar.info("Selecione a análise que deseja visualizar:")

aba = st.sidebar.selectbox(
    "---------------------------------------------",
    ["Mídias Sociais", "Ansiedade", "Saúde Mental", "Conclusão"]
)

if aba == "Mídias Sociais":
    Tab1(df).render()

elif aba == "Ansiedade":
    Tab2(df2).render()

elif aba == "Saúde Mental":
    Tab3(df3).render()

elif aba == "Conclusão":
    Tab4().render()
    
st.markdown(
    """
    <hr style="margin-top:40px; margin-bottom:20px;">
    <div style="text-align:center; color:gray; font-size:14px; background:#f9f9f9; padding:10px; border-radius:8px;">
        Desenvolvido por <b>NeuroTeam</b> 
    </div>
    """,
    unsafe_allow_html=True
)