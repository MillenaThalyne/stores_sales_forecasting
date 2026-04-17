import pandas as pd

class Dados:
    def __init__(self, path):
        self.path = path
        self.df = None

    def carregar_dados(self):
        self.df = pd.read_csv(self.path, encoding='latin-1')
        return self

    def renomear_colunas(self, key_mapping):
        self.df.rename(columns=key_mapping, inplace=True)
        return self

    def converter_tipos(self, colunas_tipos, colunas_datas=None):

        if colunas_datas:
            for coluna, formato in colunas_datas.items():
                self.df[coluna] = pd.to_datetime(
                    self.df[coluna],
                    format=formato,
                    errors='coerce'
                )

        if colunas_tipos:
            for coluna, tipo in colunas_tipos.items(): self.df[coluna] = self.df[coluna].astype(tipo)

        return self

    def salvar(self, path_saida):
        self.df.to_csv(path_saida, index=False)
        print("Dados salvos com sucesso!")
        return self