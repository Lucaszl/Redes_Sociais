import streamlit as st

class Tab4:
    def __init__(self):
        self.reference = {
            "title": "Tempo de Tela e o Cérebro - Harvard",
            "summary": [
                "O estudo realizado por Harvard analisa os efeitos do tempo excessivo em frente às telas no desenvolvimento cerebral, especialmente em adolescentes e jovens adultos.",
                "Segundo a pesquisa, o uso prolongado de mídias digitais pode aumentar níveis de ansiedade e estresse, reduzir a capacidade de atenção e concentração, afetar o sono devido à exposição à luz azul das telas e impactar o desenvolvimento emocional, dificultando habilidades sociais e empatia.",
                "O estudo reforça a importância do equilíbrio: combinar momentos digitais com atividades físicas, interações sociais presenciais e períodos de descanso é essencial para manter a saúde mental e cognitiva."
            ],
            "link": "https://hms.harvard.edu/news-events/publications-archive/brain/screen-time-brain"
        }

        # Resumo de dicas
        self.resumo = [
            "Dicas de mídia digital do pediatra e ex-cineasta Dr. Michael Rich, também conhecido como 'O Mediador':",
            "Cuidado com a distração da mídia digital. Metade de todas as crianças e três quartos dos pais sentem que o outro está distraído ao falar.",
            "Faça refeições regulares e sem tela com seus filhos.",
            "Largue o dispositivo. Esteja presente com os outros. Observe o mundo ao seu redor. Deixe sua mente vagar.",
            "Evite o uso de telas emissoras de luz azul antes de dormir.",
            "Jogue jogos online com seus filhos em vez de proibi-los. Aprenda a jogar com eles e, enquanto joga, ajude-os a pensar sobre o que estão vendo e fazendo na tela.",
            "Ajude seus filhos a planejar como gastar seu tempo, concentrando-se em atividades importantes e favoritas para evitar cair no abismo da tela."
        ]

    def render(self):
        st.markdown("<h2 style='text-align:center; color:#FF8000;'>Conclusão</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#f0f2f6;'>Resumo do estudo sobre tempo de tela e efeitos no cérebro</p>", unsafe_allow_html=True)

        
        summary_html = "".join([f"<p style='color:#333; font-size:16px;'>{para}</p>" for para in self.reference['summary']])
        st.markdown(f"""
        <div style="padding:15px; margin-bottom:15px; border-radius:8px; background-color:#f8f8ff;">
            <h3 style="color:#FF8000;">{self.reference['title']}</h3>
            {summary_html}
            <p style="text-align:right; font-size:14px; color:gray;">
                Fonte: <a href="{self.reference['link']}" target="_blank">{self.reference['title']}</a>
            </p>
        </div>
        """, unsafe_allow_html=True)

       
        dicas_html = "".join([f"<p style='color:#333; font-size:16px;'>{dica}</p>" for dica in self.resumo])
        st.markdown(f"""
        <div style="padding:15px; margin-bottom:15px; border-radius:8px; background-color:#f8f8ff;">
            <h3 style="color:#FF8000;">Dicas de mídia digital</h3>
            {dicas_html}
        </div>
        """, unsafe_allow_html=True)
