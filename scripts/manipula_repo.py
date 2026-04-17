import requests
import base64

class ManipulaRepositorios:
    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = 'meu token'
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }

    def cria_repo(self, nome_repo):
        data={
            "name": nome_repo,
            "description": "Projeto de vendas no setor de ecommerce.",
            "private": False
        }
        response = requests.post(f'{self.api_base_url}/user/repos', json=data, headers=self.headers)
        print(f'Status_code criação do repositório: {response.status_code}')

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):
        # Codificando arquivo
        with open(caminho_arquivo, 'rb') as file:
            file_content = file.read()
        encode_content = base64.b64encode(file_content)
         
        # Realizando o upload do arquivo
        url = f'{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}'
        data = {
            "message": f"Adicionando um novo arquivo: {nome_arquivo}",
            "content": encode_content.decode('utf-8')
        }

        response = requests.put(url, json=data, headers=self.headers)
        print(f'Status_code upload do arquivo: {response.status_code}')

# Criando repositório 
novo_repo = ManipulaRepositorios('MillenaThalyne')
nome_repo = 'stores_sales_forecasting'
novo_repo.cria_repo(nome_repo)

# Adicionando arquivo
nome_arquivo = 'data_processed/stores_sales_forecasting_tratado.csv'
caminho_arquivo = 'data_processed/stores_sales_forecasting_tratado.csv'
novo_repo.add_arquivo(nome_repo, nome_arquivo, caminho_arquivo)