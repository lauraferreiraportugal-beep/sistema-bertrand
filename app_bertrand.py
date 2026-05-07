import streamlit as st
from collections import Counter
from thefuzz import fuzz, process

# 1. Configuração
st.set_page_config(page_title="Bertrand Editorial AI", page_icon="🧠", layout="wide")

# 2. Estilo
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #002e5d; color: white; }
    .stChatMessage { border: 1px solid #e0e0e0; border-radius: 10px; padding: 10px; }
    h1 { color: #002e5d; font-family: 'Georgia', serif; }
    </style>
    """, unsafe_allow_html=True)

def main():
    try:
        st.sidebar.image("logo.png", width=200)
    except:
        st.sidebar.title("Bertrand")

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

    st.title("🧠 Bertrand Editorial Intelligence")
    st.markdown("##### Assistente Flexível (Pode escrever com erros!)")

    pergunta = st.chat_input("Como posso ajudar?")

    if pergunta:
        with st.chat_message("user"):
            st.write(pergunta)
        
        p = pergunta.lower()
        
        with st.chat_message("assistant"):
            # Lógica de similaridade para palavras-chave
            score_paginas = fuzz.partial_ratio(p, "páginas")
            score_autor = fuzz.partial_ratio(p, "autor")
            score_tiragem = fuzz.partial_ratio(p, "tiragem")

            # 1. Filtro de Páginas Inteligente
            if score_paginas > 70 and ("menos" in p or "abaixo" in p or "ate" in p):
                try:
                    num = int(''.join(filter(str.isdigit, p)))
                    res = [f"📖 **{t}** ({d['páginas']} pág.)" for t, d in livros.items() if d['páginas'] < num]
                    st.write(f"Encontrei estes títulos até {num} páginas:")
                    for r in res: st.write(r)
                except: st.write("Indica o número de páginas.")

            # 2. Ranking Inteligente
            elif score_autor > 70 and ("mais" in p or "top" in p):
                contagem = Counter([d['autor'] for d in livros.values()])
                autor_top, qtd = contagem.most_common(1)[0]
                st.write(f"O autor com mais títulos é **{autor_top}**.")

            # 3. Pesquisa Global Flexível (Título, Autor ou Género)
            else:
                resultados = []
                for titulo, info in livros.items():
                    # Verifica se o que foi escrito é parecido com o título, autor ou género
                    s1 = fuzz.partial_ratio(p, titulo.lower())
                    s2 = fuzz.partial_ratio(p, info['autor'].lower())
                    s3 = fuzz.partial_ratio(p, info['género'].lower())
                    
                    if s1 > 80 or s2 > 80 or s3 > 80:
                        resultados.append(f"📖 **{titulo}** | {info['autor']} | {info['género']}")
                
                if resultados:
                    st.write("Acho que procuras por isto:")
                    for r in list(set(resultados)): st.write(r)
                else:
                    st.write("Não percebi bem. Podes tentar escrever de outra forma?")

if __name__ == "__main__":
    main()
