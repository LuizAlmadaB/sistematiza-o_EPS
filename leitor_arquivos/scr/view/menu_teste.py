import tkinter as tk
import sys
from pathlib import Path
src_path = Path(__file__).resolve().parent.parent.parent  # supondo que o arquivo está em src/controller
sys.path.append(str(src_path))

from scr.controller import controllerListarLayout
from scr.controller import controllerCadastarLayout
from scr.controller import controllerProcessarArquivo

def criar_interface():
    root = tk.Tk()
    root.title("Sistema de Processamento de Arquivos")
    root.geometry("400x300")


    def abrir_consulta():
        layouts_cadastrados = controllerListarLayout.listar_layouts()
        consulta_janela = tk.Toplevel(root)
        consulta_janela.title("Layouts Cadastrados")
        tk.Label(consulta_janela, text="Layouts Cadastrados: ").pack(pady=10, padx=20)
        for layout in layouts_cadastrados:
            tk.Label(consulta_janela, text=layout).pack()
        
   
    botao_consultar = tk.Button(root, text="Consultar", width=20, command=lambda:abrir_consulta())
    botao_teste = tk.Button(root, text="Teste", command=lambda: print("teste"))
    botao_consultar.pack()
    botao_teste.pack()
    root.mainloop()

criar_interface()