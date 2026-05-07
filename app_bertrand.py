import streamlit as st
from collections import Counter

# 1. Configuração da Página
st.set_page_config(page_title="Bertrand Editorial AI", page_icon="🧠", layout="wide")

# 2. Estilo Visual Bertrand
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
        
    st.sidebar.title("Comandos Úteis")
    st.sidebar.write("- 'Quem tem mais livros?'")
    st.sidebar.write("- 'Resumo do catálogo'")
    st.sidebar.write("- 'Custo de 500 páginas'")
    
    st.title("🧠 Bertrand Editorial Intelligence")
    st.markdown("##### Assistente para Apoio à Decisão e Planeamento")

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

    pergunta = st.chat_input("Como posso ajudar a Bertrand hoje?")

    if pergunta:
        with st.chat_message("user"):
            st.write(pergunta)
        
        p = pergunta.lower()
        
        with st.chat_message("assistant"):
            # LÓGICA DE CÁLCULO E RANKING
            if "mais livros" in p:
                contagem = Counter([d['autor'] for d in livros.values()])
                autor_top, qtd = contagem.most_common(1)[0]
                st.write(f"O autor com mais títulos é **{autor_top}** ({qtd} livros).")

            elif "resumo" in p:
                st.write(f"Catálogo atual: **{len(livros)} títulos**.")
                st.write(f"Tiragem total: **{sum(d['tiragem'] for d in livros.values()):,} exemplares**.")

            elif "custo" in p:
                try:
                    num = int(''.join(filter(str.isdigit, p)))
                    st.write(f"Custo estimado para {num} páginas: **{num * 0.03:.2f}€/unidade**.")
                except: st.write("Indique o número de páginas.")

            # LÓGICA DE PESQUISA UNIVERSAL (A "MAGIA" PARA TER TODAS AS RESPOSTAS)
            else:
                resultados = []
                for titulo, info in livros.items():
                    # Se a palavra que o utilizador escreveu estiver no Título, Autor ou Género
                    if p in titulo.lower() or p in info['autor'].lower() or p in info['género'].lower():
                        resultados.append(f"📖 **{titulo}** | {info['autor']} | {info['género']} | {info['páginas']} pág. | Tiragem: {info['tiragem']:,}")
                
                if resultados:
                    st.write("Encontrei estas informações na base de dados:")
                    for r in resultados:
                        st.write(r)
                else:
                    st.write("Infelizmente não encontrei essa informação. Tente pesquisar por um nome de autor, título ou género específico.")

if __name__ == "__main__":
    main()
