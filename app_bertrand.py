import streamlit as st

# Configuração da página para parecer profissional
st.set_page_config(page_title="Portal IT Bertrand", page_icon="📚")


def main():
    st.title(" Sistema de Gestão Editorial Bertrand")
    st.subheader("Consulta de Catálogo e Tiragens")

    # A nossa base de dados de 20 livros
    livros = {
        "O Memorial do Convento": {"autor": "José Saramago", "paginas": 448, "ano": 1982, "tiragem": "50.000",
                                   "genero": "Romance Histórico"},
        "A Sibila": {"autor": "Agustina Bessa-Luís", "paginas": 256, "ano": 1954, "tiragem": "15.000",
                     "genero": "Ficção"},
        "Ensaio Sobre a Cegueira": {"autor": "José Saramago", "paginas": 312, "ano": 1995, "tiragem": "100.000",
                                    "genero": "Ficção Distópica"},
        "Equador": {"autor": "Miguel Sousa Tavares", "paginas": 528, "ano": 2003, "tiragem": "200.000",
                    "genero": "Romance"},
        "O Alquimista": {"autor": "Paulo Coelho", "paginas": 208, "ano": 1988, "tiragem": "150.000",
                         "genero": "Espiritualidade"},
        "A Menina que Roubava Livros": {"autor": "Markus Zusak", "paginas": 480, "ano": 2005, "tiragem": "80.000",
                                        "genero": "Drama Histórico"},
        "O Principezinho": {"autor": "Antoine de Saint-Exupéry", "paginas": 96, "ano": 1943, "tiragem": "30.000",
                            "genero": "Infantil"},
        "O Homem Mais Feliz do Mundo": {"autor": "Eddie Jaku", "paginas": 208, "ano": 2020, "tiragem": "25.000",
                                        "genero": "Biografia"},
        "O Código Da Vinci": {"autor": "Dan Brown", "paginas": 432, "ano": 2003, "tiragem": "120.000",
                              "genero": "Thriller"},
        "A Metamorfose": {"autor": "Franz Kafka", "paginas": 104, "ano": 1915, "tiragem": "10.000",
                          "genero": "Clássico"},
        "Os Maias": {"autor": "Eça de Queirós", "paginas": 736, "ano": 1888, "tiragem": "40.000", "genero": "Realismo"},
        "Mensagem": {"autor": "Fernando Pessoa", "paginas": 120, "ano": 1934, "tiragem": "60.000", "genero": "Poesia"},
        "O Retrato de Dorian Gray": {"autor": "Oscar Wilde", "paginas": 224, "ano": 1890, "tiragem": "20.000",
                                     "genero": "Clássico"},
        "Cem Anos de Solidão": {"autor": "Gabriel García Márquez", "paginas": 416, "ano": 1967, "tiragem": "90.000",
                                "genero": "Realismo Mágico"},
        "O Hobbit": {"autor": "J.R.R. Tolkien", "paginas": 310, "ano": 1937, "tiragem": "110.000",
                     "genero": "Fantasia"},
        "Sapiens": {"autor": "Yuval Noah Harari", "paginas": 464, "ano": 2011, "tiragem": "75.000",
                    "genero": "História/Ensaio"},
        "A Quinta dos Animais": {"autor": "George Orwell", "paginas": 112, "ano": 1945, "tiragem": "55.000",
                                 "genero": "Sátira Política"},
        "O Diário de Anne Frank": {"autor": "Anne Frank", "paginas": 352, "ano": 1947, "tiragem": "200.000",
                                   "genero": "Biografia/História"},
        "Livro do Desassossego": {"autor": "Fernando Pessoa", "paginas": 512, "ano": 1982, "tiragem": "45.000",
                                  "genero": "Ficção/Poesia"},
        "As Intermitências da Morte": {"autor": "José Saramago", "paginas": 208, "ano": 2005, "tiragem": "70.000",
                                       "genero": "Ficção"}
    }

    # Barra lateral com informação do estágio
    st.sidebar.image("https://www.bertrand.pt/img/bertrand_logo.png", width=200)  # Exemplo de logo
    st.sidebar.title("Área de IT")
    st.sidebar.info("Projeto desenvolvido para consulta rápida de dados editoriais.")

    # Seleção do Livro através de um menu Dropdown
    lista_livros = sorted(list(livros.keys()))
    livro_escolhido = st.selectbox("Selecione um livro para consultar:", ["-- Selecione --"] + lista_livros)

    if livro_escolhido != "-- Selecione --":
        st.divider()
        st.header(f"📖 {livro_escolhido}")

        # Organização em colunas para ficar visualmente bonito
        col1, col2 = st.columns(2)
        dados = livros[livro_escolhido]

        with col1:
            st.markdown(f"**👤 Autor:** {dados['autor']}")
            st.markdown(f"**🏷️ Género:** {dados['genero']}")
            st.markdown(f"**📅 Ano de Lançamento:** {dados['ano']}")

        with col2:
            st.markdown(f"**📄 Número de Páginas:** {dados['paginas']}")
            st.markdown(f"**📈 Tiragem Registada:** {dados['tiragem']} exemplares")

        st.success("Dados carregados com sucesso.")


if __name__ == "__main__":
    main()
