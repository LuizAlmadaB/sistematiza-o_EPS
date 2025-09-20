import sys
import pandas as pd
from pathlib import Path

src_path = Path(__file__).resolve().parent.parent  
sys.path.append(str(src_path))

from model.layout_arquivo import layout_arquivo
import scr.controller.controllerProcessarArquivo as controllerProcessarArquivo


def gravar_excel(arquivo_processado, nome_arquivo ,data_arquivo):
    nome_arquivo = f"{nome_arquivo}_{data_arquivo}_processado.xlsx"

    with pd.ExcelWriter(nome_arquivo) as writer:
        arquivo_processado.to_excel(writer, index=False)

