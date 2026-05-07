import streamlit as st
from collections import Counter
from thefuzz import fuzz

# 1. Configuração da Página (Mantido)
st.set_page_config(page_title="Bertrand Editorial AI", page_icon="📖", layout="wide")

# 2. Estilo Visual Bertrand (Mantido)
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #002e5d; color: white; }
    div[data-testid="stMetric"] {
        background-color: #f8f9fa;
        border-left: 5px solid #002e5d;
        padding: 15px;
        border-radius: 5px;
    }
    h1, h2, h3 { color: #002e5d !important; font-family: 'Georgia', serif; }
    .stChatMessage { border: 1px solid #e0e0e0; border-radius: 10px; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Barra Lateral com Logo (Mantido)
    try:
        st.sidebar.image("logo.png", width=200)
    except:
        st.sidebar.title("Bertrand")
    
    st.sidebar.markdown("---")
    st.sidebar.write("📌 **Projeto de Estágio**")
    st.sidebar.info("Assistente Inteligente para consulta de catálogo e apoio à decisão.")

    st.title("SISTEMA DE GESTÃO EDITORIAL")
    
    # Base de Dados Completa (Mantido)
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

    pergunta = st.chat_input("Como posso ajudar o departamento hoje?")

    if pergunta:
        with st.chat_message("user"):
            st.write(pergunta)
        
        p = pergunta.lower()
        
        with st.chat_message("assistant"):
            # Lógica de Similaridade (A nova funcionalidade de entender erros)
            score_pag = fuzz.partial_ratio(p, "páginas")
            score_tir = fuzz.partial_ratio(p, "tiragem")
            score_res = fuzz.partial_ratio(p, "resumo")
            score_aut_top = fuzz.partial_ratio(p, "mais livros")

            # 1. Filtro de Páginas (Entende 'pajinas', 'pagna', etc.)
            if score_pag > 70 and ("menos" in p or "abaixo" in p or "ate" in p):
                try:
                    num = int(''.join(filter(str.isdigit, p)))
                    res = [t for t, d in livros.items() if d['páginas'] < num]
                    st.write(f"Livros com menos de {num} páginas:")
                    for r in res: st.write(f"📖 **{r}** ({livros[r]['páginas']} pp.)")
                except: st.write("Indique o número de páginas.")

            # 2. Tiragem e Médias (Nova funcionalidade mantida)
            elif score_tir > 70:
                autor = next((d['autor'] for d in livros.values() if fuzz.partial_ratio(p, d['autor'].lower()) > 85), None)
                genero = next((d['género'] for d in livros.values() if fuzz.partial_ratio(p, d['género'].lower()) > 85), None)
                
                if autor:
                    tirs = [d['tiragem'] for d in livros.values() if d['autor'] == autor]
                    media = sum(tirs)/len(tirs)
                    st.metric(f"Média de Tiragem: {autor}", f"{int(media):,} ex.")
                elif genero:
                    tirs = [d['tiragem'] for d in livros.values() if d['género'] == genero]
                    st.metric(f"Média de Tiragem: {genero}", f"{int(sum(tirs)/len(tirs)):,} ex.")
                else: st.write("Sobre qual autor ou género deseja saber a tiragem?")

            # 3. Quem tem mais livros (Nova funcionalidade mantida)
            elif score_aut_top > 70:
                contagem = Counter([d['autor'] for d in livros.values()])
                autor_top, qtd = contagem.most_common(1)[0]
                st.write(f"O autor com maior volume no catálogo é **{autor_top}** com **{qtd} títulos**.")

            # 4. Resumo do Catálogo (Mantido)
            elif score_res > 70:
                col1, col2 = st.columns(2)
                col1.metric("Total Títulos", len(livros))
                col2.metric("Tiragem Total", f"{sum(d['tiragem'] for d in livros.values()):,}")

            # 5. Pesquisa Universal (Entende erros em nomes de livros/autores)
            else:
                achou = False
                for t, d in livros.items():
                    if fuzz.partial_ratio(p, t.lower()) > 85 or fuzz.partial_ratio(p, d['autor'].lower()) > 85:
                        st.write(f"### {t}")
                        m1, m2, m3 = st.columns(3)
                        m1.metric("Páginas", d['páginas'])
                        m2.metric("Ano", d['ano'])
                        m3.metric("Tiragem", f"{d['tiragem']:,}")
                        st.write(f"**🖋️ Autor:** {d['autor']} | **📚 Género:** {d['género']}")
                        achou = True
                        break # Mostra o mais provável
                
                if not achou:
                    st.write("Não encontrei dados exatos. Tente perguntar por 'tiragem de Saramago' ou 'livros com menos de 200 páginas'.")

    st.markdown("<br><hr><center>© 2024 Bertrand Editora | Gestão Inteligente</center>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
