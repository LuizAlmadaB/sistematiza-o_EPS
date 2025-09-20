import json

def apagar_layout(nome_layout):

    caminho_arquivo = r'leitor_arquivos\scr\controller\layouts.json'

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)

        if nome_layout in dados:
            del dados[nome_layout]
            with open(caminho_arquivo, "w", encoding="utf-8") as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)
            print(f"Layout '{nome_layout}' removido com sucesso.")
        else:
            print(f"Layout '{nome_layout}' não encontrado.")
    except Exception as e:
        print(f"Erro ao apagar layout: {e}")

