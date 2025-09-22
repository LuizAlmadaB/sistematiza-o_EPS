import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
import sys
from pathlib import Path
src_path = Path(__file__).resolve().parent.parent.parent  
sys.path.append(str(src_path))

from scr.controller import controllerCadastarLayout
from scr.controller import controllerProcessarArquivo
from scr.controller import controllerListarLayout
from scr.controller import controllerGravarArquivo
from scr.controller import controllerApagarLayout

LAYOUTS_FILE = 'leitor_arquivos/scr/controller/layouts.json'

# Função para carregar layouts existentes
def carregar_layouts():
    if os.path.exists(LAYOUTS_FILE):
        with open(LAYOUTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


# Janela principal
root = tk.Tk()
root.title("Sistema de Processamento de Arquivos Posicionais")
root.geometry("400x200")

#Cadastrar Layout
def abrir_cadastro_layout():
    cadastro = tk.Toplevel(root)
    cadastro.title("Cadastrar Novo Layout")

    tk.Label(cadastro, text="Sistema:").pack()
    sistema_entry = tk.Entry(cadastro)
    sistema_entry.pack()

    tk.Label(cadastro, text="Nome do Arquivo:").pack()
    nome_arquivo_entry = tk.Entry(cadastro)
    nome_arquivo_entry.pack()

    tk.Label(cadastro, text="Nomes das Colunas (separadas por vírgula):").pack()
    colunas_entry = tk.Entry(cadastro)
    colunas_entry.pack()

    tk.Label(cadastro, text="Tamanhos das Colunas (separados por vírgula):").pack()
    tamanhos_entry = tk.Entry(cadastro)
    tamanhos_entry.pack()

    def confirmar():
        sistema = sistema_entry.get()
        nome_arquivo = nome_arquivo_entry.get()
        colunas = colunas_entry.get().split(',')
        tamanhos = tamanhos_entry.get().split(',')

        if len(colunas) != len(tamanhos):
            messagebox.showerror("Erro", "Número de colunas e tamanhos não corresponde.")
            return

        layout = {
            "sistema": sistema,
            "nome_arquivo": nome_arquivo,
            "colunas": colunas,
            "tamanhos": [int(tamanho.strip()) for tamanho in tamanhos]
        }

        # Confirmação
        confirm = messagebox.askyesno("Confirmar", f"Confirma os dados?\n\n{json.dumps(layout, indent=2)}")
        if confirm:
            controllerCadastarLayout.criar_novo_layout(layout["sistema"], layout["nome_arquivo"], layout["colunas"], layout["tamanhos"])
            messagebox.showinfo("Sucesso", "Layout cadastrado com sucesso!")
            cadastro.destroy()

    tk.Button(cadastro, text="Confirmar Cadastro", command=confirmar).pack(pady=10)

#Consultar Layouts
def abrir_consulta_layouts():
    consulta = tk.Toplevel(root)
    consulta.title("Layouts Cadastrados")

    layouts = controllerListarLayout.listar_layouts()
    for nome in layouts:
        tk.Label(consulta, text=f"{nome}").pack(anchor='w')

#Processar Arquivo
def abrir_processar_layout():
    processar = tk.Toplevel(root)
    processar.title("Processar Arquivo")

    tk.Label(processar, text="Selecione o layout:").pack()
    layouts = carregar_layouts()
    nomes_layouts = list(layouts.keys())

    combo = ttk.Combobox(processar, values=nomes_layouts)
    combo.pack()

    tk.Label(processar, text="Data do arquivo:").pack()
    data_arquivo = tk.Entry(processar)
    data_arquivo.pack()

    def executar():
        nome = combo.get()
        if nome not in layouts:
            messagebox.showerror("Erro", "Layout não encontrado.")
            return
        arquivo = filedialog.askopenfile()
        arquivo_processado = controllerProcessarArquivo.processar_arquivo_total(arquivo, nome)
        controllerGravarArquivo.gravar_excel(arquivo_processado, nome, data_arquivo.get())
        messagebox.showinfo("Sucesso", f"Arquivo '{nome}' processado com sucesso!")

    tk.Button(processar, text="Processar", command=executar).pack(pady=10)


def abrir_menu_exclusao():
    janela = tk.Toplevel(root)
    janela.title("Excluir Layout")

    tk.Label(janela, text="Selecione o layout para excluir:").pack(pady=5)

    nomes_layouts = controllerListarLayout.listar_layouts()

    combo = ttk.Combobox(janela, values=nomes_layouts)
    combo.pack(pady=5)

    def confirmar_exclusao():
        nome = combo.get()
        if nome:
            resposta = messagebox.askyesno("Confirmação", f"Deseja excluir o layout '{nome}'?")
            if resposta:
                controllerApagarLayout.apagar_layout(nome)
                messagebox.showinfo("Sucesso", f"Layout '{nome}' excluído.")
                janela.destroy()
        else:
            messagebox.showwarning("Aviso", "Selecione um layout.")

    tk.Button(janela, text="Excluir", command=confirmar_exclusao).pack(pady=10)


# Botões principais
tk.Button(root, text="Processar Arquivo", command=abrir_processar_layout).pack(pady=10)
tk.Button(root, text="Consultar Layouts", command=abrir_consulta_layouts).pack(pady=10)
tk.Button(root, text="Cadastrar Layout", command=abrir_cadastro_layout).pack(pady=10)
tk.Button(root, text="Apagar Layout", command=abrir_menu_exclusao).pack(pady=10)

root.mainloop()