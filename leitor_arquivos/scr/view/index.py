import sys
import os
import tkinter
from tkinter import filedialog
from pathlib import Path
src_path = Path(__file__).resolve().parent.parent.parent  # supondo que o arquivo está em src/controller
sys.path.append(str(src_path))

import menu_cadastrar
import menu_listar
import menu_processar

def menu_principal():
    print("Escolha uma das opções: ")
    print("1 - Consultar Layouts")
    print("2 - Cadastrar Novo Layout")
    print("3 - Processar Arquivo")
    print("0 - Sair")
    opcao = input("Informe a opção desejada: ")

    if opcao == "1":
        menu_listar.menu_listar()
    
    elif opcao == "2":
        menu_cadastrar.menu_cadastrar()
    
    elif opcao == "3":
        pass

    elif opcao == "0":
        pass

    else:
        print("Opção inválida!")

menu_principal()
