import streamlit as st
from thefuzz import fuzz

# 1. Configuração e Estilo Bertrand
st.set_page_config(page_title="Bertrand Editorial AI", page_icon="📖", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #002e5d; color: white; }
    [data-testid="stSidebar"] div[data-testid="stMetricValue"] { color: white !important; font-size: 1.8em; }
    [data-testid="stSidebar"] div[data-testid="stMetricLabel"] { color: #d1d1d1 !important; }
    h1 { color: #002e5d !important; font-family: 'Georgia', serif; text-align: center; margin-top: 20px; }
    div[data-testid="stChatInput"] { position: relative !important; bottom: auto !important; margin-top: 50px !important; margin-bottom: 30px !important; }
    .custom-footer { position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; padding: 10px; background-color: white; border-top: 1px solid #e0e0e0; color: #1e1e1e; z-index: 999; }
    div[data-testid="stMetric"] { background-color: #f8f9fa; border-left: 5px solid #002e5d; padding: 15px; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

def main():
    livros = {
        "O Memorial do Convento": {"autor": "José Saramago", "páginas": 448, "ano": 1982, "tiragem": 50000, "género": "Romance Histórico"},
        "A Sibila": {"autor": "Agustina Bessa-Luís", "páginas": 256, "ano": 1954, "tiragem": 15000, "género": "Ficção"},
        "Ensaio Sobre a Cegueira": {"autor": "José Saramago", "páginas": 312, "ano": 1995, "tiragem": 100000, "género": "Ficção Distópica"},
        "Equador": {"autor": "Miguel Sousa Tavares", "páginas": 528, "ano": 2003, "tiragem": 200000, "género": "Romance"},
        "O Alquimista": {"autor": "Paulo Coelho", "páginas": 208, "ano": 1988, "tiragem": 150000, "género": "Espiritualidade"},
        "A Menina que Roubava Livros": {"autor": "Markus Zusak", "páginas": 480, "ano": 2005, "tiragem": 80000, "género": "Drama Histórico"},
        "O Principezinho": {"autor": "Antoine de Saint-Exupéry", "páginas": 96, "ano": 1943, "tiragem": 30000, "género": "Infantil"},
        "O Homem Mais Feliz do Mundo": {"autor": "Eddie Jaku", "páginas": 208, "ano": 2020, "tiragem": 25000, "género": "Biografia"},
        "O Código Da Vinci": {"autor": "Dan Brown", "páginas": 432, "ano": 2003, "tiragem": 120000, "género": "Thriller"},
        "A Metamorfose": {"autor": "Franz Kafka", "páginas": 104, "ano": 1915, "tiragem": 10000, "género": "Clássico"},
        "Os Maias": {"autor": "Eça de Queirós", "páginas": 736, "ano": 1888, "tiragem": 40000, "género": "Realismo"},
        "Mensagem": {"autor": "Fernando Pessoa", "páginas": 120, "ano": 1934, "tiragem": 60000, "género": "Poesia"},
        "O Retrato de Dorian Gray": {"autor": "Oscar Wilde", "páginas": 224, "ano": 1890, "tiragem": 20000, "género": "Clássico"},
        "Cem Anos de Solidão": {"autor": "Gabriel García Márquez", "páginas": 416, "ano": 1967, "tiragem": 90000, "género": "Realismo Mágico"},
        "O Hobbit": {"autor": "J.R.R. Tolkien", "páginas": 310, "ano": 1937, "tiragem": 110000, "género": "Fantasia"},
        "Sapiens": {"autor": "Yuval Noah Harari", "páginas": 464, "ano": 2011, "tiragem": 75000, "género": "História/Ensaio"},
        "A Quinta dos Animais": {"autor": "George Orwell", "páginas": 112, "ano": 1945, "tiragem": 55000, "género": "Sátira Política"},
        "O Diário de Anne Frank": {"autor": "Anne Frank", "páginas": 352, "ano": 1947, "tiragem": 200000, "género": "Biografia/História"},
        "Livro do Desassossego": {"autor": "Fernando Pessoa", "páginas": 512, "ano": 1982, "tiragem": 45000, "género": "Ficção/Poesia"},
        "As Intermitências da Morte": {"autor": "José Saramago", "páginas": 208, "ano": 2005, "tiragem": 70000, "género": "Ficção"}
    }

    with st.sidebar:
        st.markdown("### 📊 Visão Geral")
        st.metric("Títulos no Sistema", len(livros))
        st.metric("Total Tiragem", f"{sum(d['tiragem'] for d in livros.values()):,}")
        st.markdown("---")
        st.write("📌 **Projeto de Estágio**")

    st.title("SISTEMA DE GESTÃO EDITORIAL")

    p = st.chat_input("Pergunte sobre tiragens, páginas ou autores...")

    if p:
        with st.chat_message("user"):
            st.write(p)
        
        pergunta = p.lower()
        numeros = [int(s) for s in pergunta.replace('.', '').replace(',', '').split() if s.isdigit()]
        num = numeros[0] if numeros else None
        
        with st.chat_message("assistant"):
            respondido = False
            
            # --- 1. LÓGICA MATEMÁTICA PARA TIRAGEM (CORREÇÃO CRÍTICA) ---
            if "tiragem" in pergunta and num:
                if "inferior" in pergunta or "menos" in pergunta or "abaixo" in pergunta:
                    resultados = [(t, d) for t, d in livros.items() if d['tiragem'] <= num]
                    msg = f"Livros com tiragem até {num:,}:"
                else:
                    resultados = [(t, d) for t, d in livros.items() if d['tiragem'] >= num]
                    msg = f"Livros com tiragem acima de {num:,}:"
                
                st.write(f"### {msg}")
                for t, d in resultados:
                    st.write(f"📖 **{t}** — Tiragem: {d['tiragem']:,}")
                respondido = True

            # --- 2. FILTROS DE PÁGINAS ---
            elif ("págin" in pergunta or "pp" in pergunta) and num:
                cond = (lambda x: x >= num) if "mais" in pergunta or "maior" in pergunta else (lambda x: x <= num)
                res = [f"📖 **{t}** ({d['páginas']} pp.)" for t, d in livros.items() if cond(d['páginas'])]
                st.write("Resultados encontrados:")
                for r in res: st.write(r)
                respondido = True

            # --- 3. PESQUISA UNIVERSAL (PARA TUDO O RESTO) ---
            if not respondido:
                found = []
                for t, d in livros.items():
                    texto_livro = f"{t} {d['autor']} {d['género']} {d['ano']}".lower()
                    if fuzz.partial_ratio(pergunta, texto_livro) > 85 or pergunta in texto_livro:
                        found.append((t, d))
                
                if found:
                    for t, d in found:
                        st.write(f"### {t}")
                        c1, c2, c3 = st.columns(3)
                        c1.metric("Autor", d['autor'])
                        c2.metric("Ano", d['ano'])
                        c3.metric("Páginas", d['páginas'])
                        st.write(f"**Género:** {d['género']} | **Tiragem:** {d['tiragem']:,}")
                        st.divider()
                    respondido = True

            if not respondido:
                st.warning("Não encontrei resultados exatos. Tente mudar os termos da pesquisa.")

    st.markdown("""<div class="custom-footer">© 2024 Bertrand Editora | Inteligência Editorial<br><span style="color: #888; font-size: 0.85em;">Assistente Inteligente de Gestão Editorial - Análise Completa.</span></div>""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
