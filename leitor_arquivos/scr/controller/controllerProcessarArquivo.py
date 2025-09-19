import sys
import pandas as pd
from pathlib import Path

src_path = Path(__file__).resolve().parent.parent  
sys.path.append(str(src_path))

from model.layout_arquivo import layout_arquivo
from scr.controller import controllerListarLayout

todos_layouts = controllerListarLayout.todos_layouts
lista_layouts = controllerListarLayout.listar_layouts()

def carregar_layout(nome_arquivo) -> layout_arquivo: # type: ignore

    #Verifica se o layout está cadastrado no JSON e instancia um objeto:

    if nome_arquivo in lista_layouts:
        layout_alvo = todos_layouts[nome_arquivo]
        layout = layout_arquivo(sistema=layout_alvo["sistema"], nome_arquivo=layout_alvo["nome_arquivo"], nome_colunas=layout_alvo["nome_colunas"], tamanho_colunas=layout_alvo["tamanho_colunas"])
        return layout
    else:
        print("Layout não encontrado")

def processar_arquivo_total(arquivo, layout) -> pd.DataFrame:

    layout = carregar_layout(layout)

    arquivo_processado = pd.read_fwf(arquivo, 
                widths= layout.tamanho_colunas,
                names= layout.nome_colunas,
                dtype="str")
    
    df = pd.DataFrame(arquivo_processado.drop(index=[0, arquivo_processado.index[-1]])) 
    
    return df

def processar_arquivo_por_registro(arquivo, layout, registro) -> pd.DataFrame:

    layout = carregar_layout(layout)

    arquivo_processado = pd.read_fwf(arquivo, 
                widths= layout.tamanho_colunas,
                names= layout.nome_colunas,
                dtype="str")
    
    df = pd.DataFrame(arquivo_processado.drop(index=[0, arquivo_processado.index[-1]]))
    df = df[df['tp'] == registro] 
    
    return df

