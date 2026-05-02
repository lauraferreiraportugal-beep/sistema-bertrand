def sistema_bertrand_final():
    # Base de dados com 20 livros relevantes para a Bertrand
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

    print("\n" + "=".center(65, "="))
    print("SISTEMA DE GESTÃO EDITORIAL BERTRAND".center(65))
    print("=".center(65, "="))

    while True:
        print("\n--- MENU DE SELEÇÃO ---")
        entrada = input("Indique o nome do livro (ou escreva 'lista' / 'sair'): ").strip()

        if entrada.lower() == 'sair':
            print("\nA encerrar o ficheiro de consulta...")
            break

        if entrada.lower() == 'lista':
            print("\n 📚CATÁLOGO DISPONÍVEL (20 TÍTULOS):")
            for titulo in sorted(livros.keys()):
                print(f" • {titulo}")
            continue

        # Procura o livro na base de dados (ignora maiúsculas/minúsculas)
        livro_encontrado = next((t for t in livros if t.lower() == entrada.lower()), None)

        if livro_encontrado:
            consultando_livro = True
            while consultando_livro:
                print(f"\n📖 Ficha técnica: {livro_encontrado.upper()}")
                caracteristicas = list(livros[livro_encontrado].keys())
                print(f"Informações disponíveis: {', '.join(caracteristicas)}")

                pergunta = input(f"Que informação deseja consultar? ").lower().strip()

                if pergunta in livros[livro_encontrado]:
                    resultado = livros[livro_encontrado][pergunta]
                    print(f"\n RESPOSTA: O campo '{pergunta}' de '{livro_encontrado}' é: {resultado}")

                    # Verificação inteligente (aceita 's', 'sim', 'si')
                    continuar = input(
                        "\nDeseja consultar mais alguma informação sobre ESTE livro? (s/n): ").lower().strip()
                    if not continuar.startswith('s'):
                        consultando_livro = False
                        print(f"A fechar a ficha técnica de '{livro_encontrado}'...")
                else:
                    print(f"❌ Opção inválida. Por favor, escolha: {', '.join(caracteristicas)}")

            # Verificação para novo livro ou fechar o programa
            outro_livro = input("\nDeseja pesquisar outro livro no catálogo? (s/n): ").lower().strip()
            if not outro_livro.startswith('s'):
                print("\nA sair do sistema...")
                break
        else:
            print("❌ Livro não encontrado no sistema. Por favor, verifique o título ou consulte a 'lista'.")

    print("\n Sessão terminada!👋")


if __name__ == "__main__":
    sistema_bertrand_final()