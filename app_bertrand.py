import streamlit as st

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
    # --- CORREÇÃO DE INDENTAÇÃO NA SIDEBAR ---
    try:
        st.sidebar.image("logo.png", width=200)
    except:
        st.sidebar.title("Bertrand")

    st.sidebar.title("Comandos Úteis")
    st.sidebar.write("- 'Resumo do catálogo'")
    st.sidebar.write("- 'Custo de 300 páginas'")
    st.sidebar.write("- 'Média de tiragem de Ficção'")
    
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
            # 1. RESUMO
            if "resumo" in p or "catálogo" in p:
                total_livros = len(livros)
                total_tiragem = sum(d['tiragem'] for d in livros.values())
                st.write(f"Atualmente gerimos **{total_livros} títulos**.")
                st.write(f"Volume total de impressões histórico: **{total_tiragem:,} exemplares**.")

            # 2. CUSTO
            elif "custo" in p or "preço" in p:
                try:
                    pags = int(''.join(filter(str.isdigit, p)))
                    custo_estimado = pags * 0.03
                    st.write(f"Para um livro de **{pags} páginas**, o custo base estimado é de **{custo_estimado:.2f}€** por unidade.")
                except:
                    st.write("Por favor, indique o número de páginas.")

            # 3. TIRAGEM / MÉDIAS
            elif "tiragem" in p or "impressões" in p or "méd" in p:
                filtro = next((g for t, d in livros.items() if g.lower() in p), None)
                autor = next((d['autor'] for t, d in livros.items() if d['autor'].lower() in p), None)
                
                if autor:
                    dados_autor = [d['tiragem'] for d in livros.values() if d['autor'] == autor]
                    media = sum(dados_autor) / len(dados_autor)
                    st.write(f"O autor **{autor}** tem uma média de **{int(media):,} exemplares**.")
                elif filtro:
                    dados_gen = [d['tiragem'] for d in livros.values() if d['género'] == filtro]
                    st.write(f"Média de tiragem para **{filtro}**: **{int(sum(dados_gen)/len(dados_gen)):,}**.")

            # 4. PÁGINAS
            elif "páginas" in p:
                try:
                    num = int(''.join(filter(str.isdigit, p)))
                    if "menos" in p or "abaixo" in p:
                        res = [f"📖 {t}" for t, d in livros.items() if d['páginas'] < num]
                        st.write(f"Livros com menos de {num} páginas:")
                        for r in res: st.write(r)
                except:
                    st.write("Indique o limite de páginas.")
            else:
                st.write("Ainda estou a aprender. Tente perguntar por 'tiragem de Saramago' ou 'custo de 200 páginas'.")

if __name__ == "__main__":
    main()
