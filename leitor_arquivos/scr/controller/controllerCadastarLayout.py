import sys
import os
import json
from pathlib import Path
src_path = Path(__file__).resolve().parent.parent  # supondo que o arquivo está em src/controller
sys.path.append(str(src_path))

from model.layout_arquivo import layout_arquivo

_lista_layouts = Path(__file__).resolve().parent/"layouts.json"


def criar_novo_layout(sistema, nome_arquivo, nome_colunas, tamanho_colunas) -> object:

    novo_layout = {
        "sistema": sistema,
        "nome_arquivo": nome_arquivo,
        "nome_colunas": nome_colunas,
        "tamanho_colunas": tamanho_colunas
    }
    
    # Verifica se o arquivo existe e carrega os layouts existentes
    if os.path.exists(_lista_layouts):
        with open(_lista_layouts, "r", encoding="utf-8") as f:
            try:
                todos_layouts = json.load(f)
            except json.JSONDecodeError:
                todos_layouts = {}
    else:
        todos_layouts = {}

    # Atualiza ou adiciona novo layout
    todos_layouts[nome_arquivo] = novo_layout

    # Salva o dicionário completo no arquivo
    with open(_lista_layouts, "w", encoding="utf-8") as f:
        json.dump(todos_layouts, f, ensure_ascii=False, indent=4)
