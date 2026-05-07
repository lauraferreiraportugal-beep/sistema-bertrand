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
    st.sidebar.info("Assistente Inteligente de Gestão Editorial - Análise Completa.")

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

    p = st.chat_input("Pergunte qualquer coisa (ex: 'livros de Saramago', 'mais de 300 páginas', 'tiragem total'...)")

    if p:
        with st.chat_message("user"):
            st.write(p)
        
        pergunta = p.lower()
        numeros = [int(s) for s in pergunta.split() if s.isdigit()]
        num = numeros[0] if numeros else None
        respondido = False

        with st.chat_message("assistant"):
            
            # 1. LÓGICA DE TIRAGENS TOTAIS/MÉDIAS
            if "tiragem" in pergunta or "impressões" in pergunta:
                if "total" in pergunta or "todos" in pergunta:
                    total = sum(d['tiragem'] for d in livros.values())
                    st.write(f"A tiragem total do catálogo é de **{total:,} exemplares**.")
                    respondido = True
                else:
                    # Tenta encontrar se o utilizador falou de um autor ou género
                    alvo = next((v for v in ["saramago", "pessoa", "eça", "queirós", "ficção", "romance", "clássico", "biografia"] if v in pergunta), None)
                    res = [d['tiragem'] for t, d in livros.items() if alvo and (alvo in d['autor'].lower() or alvo in d['género'].lower())]
                    if res:
                        st.write(f"A tiragem total para essa pesquisa é de **{sum(res):,} exemplares**.")
                        st.write(f"Média por livro: **{int(sum(res)/len(res)):,}**.")
                        respondido = True

            # 2. LÓGICA DE FILTROS NUMÉRICOS (Páginas e Anos)
            if not respondido and num:
                # Páginas
                if "págin" in pergunta or "pagin" in pergunta or "pp" in pergunta:
                    if "mais" in pergunta or "maior" in pergunta or "acima" in pergunta:
                        res = [f"📖 **{t}** ({d['páginas']} pp.)" for t, d in livros.items() if d['páginas'] > num]
                        st.write(f"Livros com mais de {num} páginas:")
                    else:
                        res = [f"📖 **{t}** ({d['páginas']} pp.)" for t, d in livros.items() if d['páginas'] < num]
                        st.write(f"Livros com menos de {num} páginas:")
                    for r in res: st.write(r)
                    respondido = True
                # Anos
                elif "ano" in pergunta or "lançado" in pergunta:
                    if "depois" in pergunta or "após" in pergunta or "recente" in pergunta:
                        res = [f"📖 **{t}** ({d['ano']})" for t, d in livros.items() if d['ano'] > num]
                        st.write(f"Livros lançados depois de {num}:")
                    else:
                        res = [f"📖 **{t}** ({d['ano']})" for t, d in livros.items() if d['ano'] < num]
                        st.write(f"Livros lançados antes de {num}:")
                    for r in res: st.write(r)
                    respondido = True

            # 3. LÓGICA DE CONTAGEM E LISTAGEM
            if not respondido:
                if "lista" in pergunta or "quais" in pergunta or "diz me" in pergunta or "mostra" in pergunta or "todos" in pergunta:
                    # Procura por Autor ou Género na pergunta
                    resultados = []
                    for t, d in livros.items():
                        # Super busca: título, autor ou género
                        if fuzz.partial_ratio(pergunta, t.lower()) > 80 or \
                           fuzz.partial_ratio(pergunta, d['autor'].lower()) > 80 or \
                           fuzz.partial_ratio(pergunta, d['género'].lower()) > 80:
                            resultados.append((t, d))
                    
                    if resultados:
                        st.write(f"Encontrei {len(resultados)} resultados:")
                        for t, d in resultados:
                            with st.expander(f"📖 {t} ({d['autor']})"):
                                c1, c2 = st.columns(2)
                                c1.metric("Páginas", d['páginas'])
                                c1.metric("Ano", d['ano'])
                                c2.metric("Tiragem", f"{d['tiragem']:,}")
                                c2.write(f"**Género:** {d['género']}")
                        respondido = True

            # 4. BUSCA UNITÁRIA (Fuzzy Matching para tudo o resto)
            if not respondido:
                # Se escreveu apenas um nome (ex: "Saramago")
                for t, d in livros.items():
                    if fuzz.partial_ratio(pergunta, t.lower()) > 85 or fuzz.partial_ratio(pergunta, d['autor'].lower()) > 85:
                        st.subheader(t)
                        col1, col2, col3 = st.columns(3)
                        col1.metric("Autor", d['autor'])
                        col2.metric("Páginas", d['páginas'])
                        col3.metric("Ano", d['ano'])
                        st.write(f"**Tiragem:** {d['tiragem']:,} exemplares | **Género:** {d['género']}")
                        respondido = True
                        break

            if not respondido:
                st.warning("Não consegui encontrar dados para essa pergunta. Tente pesquisar por autor, género, páginas ou tiragem.")

    st.markdown("<br><hr><center>© 2024 Bertrand Editora | Inteligência Editorial</center>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
