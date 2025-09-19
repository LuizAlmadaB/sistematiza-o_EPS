import sys
import tkinter
from tkinter import filedialog
from pathlib import Path
src_path = Path(__file__).resolve().parent.parent.parent  # supondo que o arquivo está em src/controller
sys.path.append(str(src_path))

from scr.controller import controllerGravarArquivo
from scr.controller import controllerProcessarArquivo

def menu_processar():
    print("### Processar Arquivo: ")
    print("Arquivo com mais de um tipo de registro? \n" 
    "1 - Sim \n" 
    "2 - Não \n"    
    "0 - Sair")
    opcao = input("Informe a opção desejada: ")

    while True:

        if opcao == "1":
            try:
                layout_arquivo = input("Informe o nome do arquivo (Ex: M123): ")
                registro = input("Informe o tipo de registro que deseja analisar: ")
                tkinter.Tk().withdraw()
                arquivo = filedialog.askopenfile()
                arquivo_processado = controllerProcessarArquivo.processar_arquivo_por_registro(arquivo, layout_arquivo, registro)
                controllerGravarArquivo.gravar_excel(arquivo_processado)
                print("Arquivo gravado com sucesso!")
            except Exception as e:
                print("Não foi possível processar o arquivo: {e}")
    
        elif opcao == "2":
            try:
                layout_arquivo = input("Informe o nome do arquivo (Ex: M123): ")
                tkinter.Tk().withdraw()
                arquivo = filedialog.askopenfile()
                arquivo_processado = controllerProcessarArquivo.processar_arquivo_total(arquivo, layout_arquivo)
                controllerGravarArquivo.gravar_excel(arquivo_processado)
                print("Arquivo gravado com sucesso!")
            except Exception as e:
                print("Não foi possível processar o arquivo: {e}")

        elif opcao == "0":
            break

        else:
            print("Opção informada é inválida. Tente novamente")
            break

