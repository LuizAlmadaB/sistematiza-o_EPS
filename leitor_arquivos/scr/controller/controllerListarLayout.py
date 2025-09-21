import sys
import os
import json
from pathlib import Path
src_path = Path(__file__).resolve().parent.parent  # supondo que o arquivo está em src/controller
sys.path.append(str(src_path))

from model.layout_arquivo import layout_arquivo

_lista_layouts = Path(__file__).resolve().parent/"layouts.json"
arquivo = open(_lista_layouts)
todos_layouts = json.load(arquivo)

def listar_layouts() -> list:
    
    lista_de_layouts_disponiveis = []

    for i in todos_layouts:
        lista_de_layouts_disponiveis.append(i)
    
    return lista_de_layouts_disponiveis


