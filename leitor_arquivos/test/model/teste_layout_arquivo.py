import unittest
import sys
from pathlib import Path
src_path = Path(__file__).resolve().parent.parent.parent  
sys.path.append(str(src_path))

# Supondo que a classe esteja no mesmo arquivo ou importada corretamente
from scr.model import layout_arquivo  # ajuste o nome do módulo conforme necessário

class TestLayoutArquivo(unittest.TestCase):

    def setUp(self):
        self.sistema = "sisteste"
        self.nome_arquivo = "arquivo_teste"
        self.nome_colunas = ["tp", "contrato", "nome", "valor"]
        self.tamanho_colunas = [2, 8, 20, 10]
        self.layout = layout_arquivo.layout_arquivo(self.sistema, self.nome_arquivo, self.nome_colunas, self.tamanho_colunas)

    def test_instanciacao(self):
        self.assertEqual(self.layout.sistema, self.sistema)
        self.assertEqual(self.layout.nome_arquivo, self.nome_arquivo)
        self.assertEqual(self.layout.nome_colunas, self.nome_colunas)
        self.assertEqual(self.layout.tamanho_colunas, self.tamanho_colunas)

    def test_to_dict(self):
        esperado = {
            "sistema": self.sistema,
            "nome_arquivo": self.nome_arquivo,
            "nome_colunas": [self.nome_colunas],
            "tamanho_colunas": [self.tamanho_colunas]
        }
        self.assertEqual(self.layout.to_dict(), esperado)

    def test_get_tamanho_colunas(self):
        self.assertEqual(self.layout.get_tamanho_colunas(), self.tamanho_colunas)

    def test_get_nome_arquivo(self):
        self.assertEqual(self.layout.get_nome_arquivo(), self.nome_arquivo)

if __name__ == '__main__':
    unittest.main()