class layout_arquivo:

    def __init__(self, sistema, nome_arquivo, nome_colunas, tamanho_colunas):
        self.sistema = sistema
        self.nome_arquivo = nome_arquivo
        self.nome_colunas = nome_colunas
        self.tamanho_colunas = tamanho_colunas

    
    def to_dict(self):
        return {
            "sistema": self.sistema,
            "nome_arquivo": self.nome_arquivo,
            "nome_colunas": [self.nome_colunas],
            "tamanho_colunas": [self.tamanho_colunas]
        }
    
    def get_tamanho_colunas(self):
        return self.tamanho_colunas
    
    def get_nome_arquivo(self) -> str:
        return self.nome_arquivo
