import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Portal Editorial Bertrand", page_icon="📖", layout="wide")

# 2. CSS Personalizado - Identidade Visual Bertrand
st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
    }
    [data-testid="stSidebar"] {
        background-color: #002e5d;
        color: white;
    }
    [data-testid="stSidebar"] .stMarkdown p {
        color: #f0f0f0;
    }
    div[data-testid="stMetric"] {
        background-color: #f8f9fa;
        border-left: 5px solid #002e5d;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    h1, h2, h3 {
        color: #002e5d !important;
        font-family: 'Georgia', serif;
    }
    /* Estilo para centralizar a imagem na barra lateral */
    [data-testid="stSidebar"] img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        padding-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Barra Lateral com Logótipo
    st.sidebar.image("logo.png.png", width=200)
    st.sidebar.markdown("---")
    st.sidebar.write(" **Projeto de Estágio**")
    st.sidebar.write("Consulta rápida de catálogo e métricas editoriais.")
    
    # Conteúdo Principal
    st.title("SISTEMA DE GESTÃO EDITORIAL")
    st.write("") # Espaço em branco

    # Base de Dados completa
    livros = {
        "O Memorial do Convento": {"autor": "José Saramago", "páginas": 448, "ano": 1982, "tiragem": "50.000", "género": "Romance Histórico"},
        "A Sibila": {"autor": "Agustina Bessa-Luís", "páginas": 256, "ano": 1954, "tiragem": "15.000", "género": "Ficção"},
        "Ensaio Sobre a Cegueira": {"autor": "José Saramago", "páginas": 312, "ano": 1995, "tiragem": "100.000", "género": "Ficção Distópica"},
        "Equador": {"autor": "Miguel Sousa Tavares", "páginas": 528, "ano": 2003, "tiragem": "200.000", "género": "Romance"},
        "O Alquimista": {"autor": "Paulo Coelho", "páginas": 208, "ano": 1988, "tiragem": "150.000", "género": "Espiritualidade"},
        "A Menina que Roubava Livros": {"autor": "Markus Zusak", "páginas": 480, "ano": 2005, "tiragem": "80.000", "género": "Drama Histórico"},
        "O Principezinho": {"autor": "Antoine de Saint-Exupéry", "páginas": 96, "ano": 1943, "tiragem": "30.000", "género": "Infantil"},
        "O Homem Mais Feliz do Mundo": {"autor": "Eddie Jaku", "páginas": 208, "ano": 2020, "tiragem": "25.000", "género": "Biografia"},
        "O Código Da Vinci": {"autor": "Dan Brown", "páginas": 432, "ano": 2003, "tiragem": "120.000", "género": "Thriller"},
        "A Metamorfose": {"autor": "Franz Kafka", "páginas": 104, "ano": 1915, "tiragem": "10.000", "género": "Clássico"},
        "Os Maias": {"autor": "Eça de Queirós", "páginas": 736, "ano": 1888, "tiragem": "40.000", "género": "Realismo"},
        "Mensagem": {"autor": "Fernando Pessoa", "páginas": 120, "ano": 1934, "tiragem": "60.000", "género": "Poesia"},
        "O Retrato de Dorian Gray": {"autor": "Oscar Wilde", "páginas": 224, "ano": 1890, "tiragem": "20.000", "género": "Clássico"},
        "Cem Anos de Solidão": {"autor": "Gabriel García Márquez", "páginas": 416, "ano": 1967, "tiragem": "90.000", "género": "Realismo Mágico"},
        "O Hobbit": {"autor": "J.R.R. Tolkien", "páginas": 310, "ano": 1937, "tiragem": "110.000", "género": "Fantasia"},
        "Sapiens": {"autor": "Yuval Noah Harari", "páginas": 464, "ano": 2011, "tiragem": "75.000", "género": "História/Ensaio"},
        "A Quinta dos Animais": {"autor": "George Orwell", "páginas": 112, "ano": 1945, "tiragem": "55.000", "género": "Sátira Política"},
        "O Diário de Anne Frank": {"autor": "Anne Frank", "páginas": 352, "ano": 1947, "tiragem": "200.000", "género": "Biografia/História"},
        "Livro do Desassossego": {"autor": "Fernando Pessoa", "páginas": 512, "ano": 1982, "tiragem": "45.000", "género": "Ficção/Poesia"},
        "As Intermitências da Morte": {"autor": "José Saramago", "páginas": 208, "ano": 2005, "tiragem": "70.000", "género": "Ficção"}
    }

    # Menu de Seleção
    lista_ordenada = sorted(list(livros.keys()))
    escolha = st.selectbox("📖 Selecione um título para consulta técnica:", ["-- Pesquisar no Catálogo --"] + lista_ordenada)

    if escolha != "-- Pesquisar no Catálogo --":
        dados = livros[escolha]
        
        st.write(f"### {escolha}")
        
        # Métricas (Páginas, Ano, Tiragem)
        m1, m2, m3 = st.columns(3)
        m1.metric("Páginas", f"{dados['páginas']} pp.")
        m2.metric("Publicação", dados['ano'])
        m3.metric("Tiragem (Exemplares)", dados['tiragem'])

        st.markdown("---")
        
        # Dados do autor e género
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"**🖋️ Autor:** {dados['autor']}")
        with c2:
            st.markdown(f"**📚 Género Literário:** {dados['género']}")
        
        st.success(f"Informação validada para a obra: {escolha}")
    else:
        st.info("Utilize a caixa de seleção acima para verificar os dados técnicos.")

    # Rodapé institucional
    st.write("<br><br>", unsafe_allow_html=True)
    st.divider()
    st.caption("© 2024 Bertrand Editora | Powered by IT Division")

if __name__ == "__main__":
    main()
