import streamlit as st

# Configuração da página para parecer profissional
st.set_page_config(page_title="Portal IT Bertrand", page_icon="📚")


def main():
    st.title(" Sistema de Gestão Editorial Bertrand")
    st.subheader("Consulta de Livros")

    # A nossa base de dados de 20 livros
    livros = {
        "O Memorial do Convento": {"autor": "José Saramago", "páginas": 448, "ano": 1982, "tiragem": "50.000",
                                   "género": "Romance Histórico"},
        "A Sibila": {"autor": "Agustina Bessa-Luís", "páginas": 256, "ano": 1954, "tiragem": "15.000",
                     "género": "Ficção"},
        "Ensaio Sobre a Cegueira": {"autor": "José Saramago", "páginas": 312, "ano": 1995, "tiragem": "100.000",
                                    "género": "Ficção Distópica"},
        "Equador": {"autor": "Miguel Sousa Tavares", "páginas": 528, "ano": 2003, "tiragem": "200.000",
                    "género": "Romance"},
        "O Alquimista": {"autor": "Paulo Coelho", "páginas": 208, "ano": 1988, "tiragem": "150.000",
                         "género": "Espiritualidade"},
        "A Menina que Roubava Livros": {"autor": "Markus Zusak", "páginas": 480, "ano": 2005, "tiragem": "80.000",
                                        "género": "Drama Histórico"},
        "O Principezinho": {"autor": "Antoine de Saint-Exupéry", "páginas": 96, "ano": 1943, "tiragem": "30.000",
                            "género": "Infantil"},
        "O Homem Mais Feliz do Mundo": {"autor": "Eddie Jaku", "páginas": 208, "ano": 2020, "tiragem": "25.000",
                                        "género": "Biografia"},
        "O Código Da Vinci": {"autor": "Dan Brown", "páginas": 432, "ano": 2003, "tiragem": "120.000",
                              "género": "Thriller"},
        "A Metamorfose": {"autor": "Franz Kafka", "páginas": 104, "ano": 1915, "tiragem": "10.000",
                          "género": "Clássico"},
        "Os Maias": {"autor": "Eça de Queirós", "páginas": 736, "ano": 1888, "tiragem": "40.000", "género": "Realismo"},
        "Mensagem": {"autor": "Fernando Pessoa", "páginas": 120, "ano": 1934, "tiragem": "60.000", "género": "Poesia"},
        "O Retrato de Dorian Gray": {"autor": "Oscar Wilde", "páginas": 224, "ano": 1890, "tiragem": "20.000",
                                     "género": "Clássico"},
        "Cem Anos de Solidão": {"autor": "Gabriel García Márquez", "páginas": 416, "ano": 1967, "tiragem": "90.000",
                                "género": "Realismo Mágico"},
        "O Hobbit": {"autor": "J.R.R. Tolkien", "páginas": 310, "ano": 1937, "tiragem": "110.000",
                     "género": "Fantasia"},
        "Sapiens": {"autor": "Yuval Noah Harari", "páginas": 464, "ano": 2011, "tiragem": "75.000",
                    "género": "História/Ensaio"},
        "A Quinta dos Animais": {"autor": "George Orwell", "páginas": 112, "ano": 1945, "tiragem": "55.000",
                                 "género": "Sátira Política"},
        "O Diário de Anne Frank": {"autor": "Anne Frank", "páginas": 352, "ano": 1947, "tiragem": "200.000",
                                   "género": "Biografia/História"},
        "Livro do Desassossego": {"autor": "Fernando Pessoa", "páginas": 512, "ano": 1982, "tiragem": "45.000",
                                  "género": "Ficção/Poesia"},
        "As Intermitências da Morte": {"autor": "José Saramago", "páginas": 208, "ano": 2005, "tiragem": "70.000",
                                       "género": "Ficção"}
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
