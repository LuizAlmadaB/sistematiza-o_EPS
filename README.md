# 📊 Leitor de Arquivos Posicionais

## 🧭 Introdução

Esta é uma aplicação para **processamento de arquivos posicionais**, transformando-os em **tabelas** para facilitar a análise de seu conteúdo.

Antes de realizar o processamento de qualquer arquivo, é necessário que haja um **layout previamente cadastrado**. O layout define:

- Quais são as informações do arquivo (colunas)
- Qual o tamanho de cada campo

Com isso, a aplicação realiza a **divisão correta da string** e a transforma em um **DataFrame** utilizando a biblioteca `pandas`.

---

## ⚙️ Funcionalidades

- **Cadastrar Layouts**  
  Permite que o usuário cadastre o layout de um arquivo, informando:
  - Sistema de origem
  - Nome do arquivo (ex: `M123`, `clientesret`)
  - Colunas e seus respectivos tamanhos

- **Consultar Layouts**  
  Permite ao usuário visualizar os layouts já salvos no sistema.

- **Apagar Layouts**  
  Permite ao usuário excluir layouts previamente cadastrados.

- **Processar Arquivo**  
  Permite ao usuário processar um arquivo posicional em uma tabela, de acordo com o layout selecionado.  
  O layout deve ser escolhido **antes do upload** do arquivo.

> ⚠️ **Atenção:** A seleção de um layout incorreto poderá resultar em **resultados inconsistentes** no arquivo final.

---

## 🗂️ Estrutura do Projeto

A aplicação foi construída utilizando a arquitetura **MVC** e segue a seguinte estrutura de pastas:

📁 Model ├── layout_arquivo.py Classe utilizada para instanciar objetos que representam o layout do arquivo, permitindo acesso às informações de colunas e tamanho.
📁 Controller ├── controllerProcessarArquivo.py Realiza a conversão do arquivo posicional em uma tabela, utilizando a biblioteca Pandas e o objeto do tipo "layout_arquivo".
├── controllerGravarArquivo.py Recebe um arquivo processado e gera um arquivo .xlsx.
├── controllerCadastarLayout.py Responsável pela gravação de um novo layout no arquivo layouts.json.
├── controllerListarLayout.py Verifica quais layouts estão salvos em layouts.json.
├── controllerApagarLayout.py Remove um layout de layouts.json.


---

## 📋 Requisitos

- Python **3.10+**
- Biblioteca **Pandas**
- Interface gráfica com **Tkinter**
