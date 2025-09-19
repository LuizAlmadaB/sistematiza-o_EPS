import sys
from pathlib import Path
src_path = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(src_path))

from scr.controller import controllerCadastarLayout


def menu_cadastrar():
    print("#### Cadastrar Novo Layout ###")
    sistema = input("Informe o nome do sistema ao qual o layout de arquivo pertence: ")
    nome_arquivo = input("Informe o nome do arquivo cujo layout será cadastrado: ")
    nome_colunas = input("Informe o nome de CADA coluna do layout separado por vírgula (ex: nome, idade, contrato): ")
    tamanho_colunas = input("Informe o tamanho de cada coluna separado por vírgula (ex: 20, 2, 17): ")

    try:
        controllerCadastarLayout.criar_novo_layout(sistema=sistema, nome_arquivo=nome_arquivo, nome_colunas=nome_colunas, tamanho_colunas=tamanho_colunas)
        print(f"Layout do arquivo {nome_arquivo} cadastrado com sucesso!")
    except Exception as e:
        print("Erro ao gravar o layout: {e}")



