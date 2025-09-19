import unittest

from leitor_arquivos.scr.model.layout_arquivo import layout_arquivo


class testLayoutArquivo(unittest.TestCase):

    def setUp(self):
        self.layout_arquivo = layout_arquivo("siapi", "m123", ["tp", "nome", "contrato"], [1, 25, 17])
    
    def test_criacao(self):
        self.assertIsInstance(self.layout_arquivo, layout_arquivo)