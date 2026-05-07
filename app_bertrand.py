import streamlit as st
from thefuzz import fuzz
from collections import Counter

# 1. Configuração e Estilo Bertrand
st.set_page_config(page_title="Bertrand Editorial AI", page_icon="📖", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #002e5d; color: white; }
    div[data-testid="stMetric"] { background-color: #f8f9fa; border-left: 5px solid #002e5d; padding: 15px; border-radius: 5px; }
    h1, h2, h3 { color: #002e5d !important; font-family: 'Georgia', serif; }
    .stChatMessage { border: 1px solid #e0e0e0; border-radius: 10px; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

def main():
    try:
        st.sidebar.image("logo.png", width=200)
    except:
        st.sidebar.title("Bertrand")
    
    st.sidebar.markdown("---")
    st.sidebar.info("Assistente Inteligente Acumulativo - Gestão de Inventário.")

    st.title("SISTEMA DE GESTÃO EDITORIAL")
    
    # Base de Dados
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

    pergunta = st.chat_input("Diga-me o que procura...")

    if pergunta:
        with st.chat_message("user"):
            st.write(pergunta)
        
        p = pergunta.lower()
        
        with st.chat_message("assistant"):
            numeros = [int(s) for s in p.split() if s.isdigit()]
            num = numeros[0] if numeros else None
            respondido = False

            # --- A) FILTRO DINÂMICO: PÁGINAS (MAIS OU MENOS) ---
            if num and ("págin" in p or "pagin" in p or "pp" in p):
                if "mais" in p or "maior" in p or "acima" in p:
                    res = [f"📖 **{t}** ({d['páginas']} pp.)" for t, d in livros.items() if d['páginas'] > num]
                    texto = "mais"
                else:
                    res = [f"📖 **{t}** ({d['páginas']} pp.)" for t, d in livros.items() if d['páginas'] < num]
                    texto = "menos"
                
                st.write(f"Livros com {texto} de {num} páginas:")
                for r in res: st.write(r)
                respondido = True

            # --- B) FILTRO DINÂMICO: ANOS (ANTES OU DEPOIS) ---
            elif num and ("ano" in p or "lançado" in p):
                if "depois" in p or "após" in p or "mais recente" in p:
                    res = [f"📖 **{t}** ({d['ano']})" for t, d in livros.items() if d['ano'] > num]
                    texto = "depois de"
                else:
                    res = [f"📖 **{t}** ({d['ano']})" for t, d in livros.items() if d['ano'] < num]
                    texto = "antes de"
                
                st.write(f"Livros {texto} {num}:")
                for r in res: st.write(r)
                respondido = True

            # --- C) COMANDOS GERAIS (LISTA, TIRAGEM, RANKING) ---
            elif "lista" in p or "todos" in p:
                st.write("### Catálogo Completo:")
                for t in sorted(livros.keys()):
                    st.write(f"📖 **{t}** — {livros[t]['autor']}")
                respondido = True

            elif "tiragem" in p and ("total" in p or "todos" in p):
                total = sum(d['tiragem'] for d in livros.values())
                st.write(f"A tiragem total registada é de **{total:,} exemplares**.")
                respondido = True

            # --- D) PESQUISA UNIVERSAL (MÉTRICAS) ---
            if not respondido:
                resultados = []
                for t, d in livros.items():
                    conhecimento = f"{t} {d['autor']} {d['género']} {d['ano']}".lower()
                    if fuzz.partial_ratio(p, conhecimento) > 80 or p in conhecimento:
                        resultados.append((t, d))
                
                if resultados:
                    for t, d in resultados:
                        st.write(f"### {t}")
                        c1, c2, c3 = st.columns(3)
                        c1.metric("Autor", d['autor'])
                        c2.metric("Ano", d['ano'])
                        c3.metric("Páginas", d['páginas'])
                        st.write(f"**Tiragem:** {d['tiragem']:,} ex | **Género:** {d['género']}")
                        st.divider()
                    respondido = True

            if not respondido:
                st.write("Infelizmente não consegui processar esse pedido. Tente ser mais específico.")

if __name__ == "__main__":
    main()
