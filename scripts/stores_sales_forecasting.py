from processamento_dados import Dados

# Caminho dos dados
path = 'data_raw/stores_sales_forecasting.csv'

# Mapeamento de colunas
key_mapping = {
    'Row ID': 'ID Registro',
    'Order ID': 'ID Pedido',
    'Order Date': 'Data do Pedido',
    'Ship Date': 'Data de Envio Pedido',
    'Ship Mode': 'Modo de Envio Pedido',
    'Customer ID': 'ID Cliente',
    'Customer Name': 'Nome Cliente',
    'Segment': 'Classificacao Cliente',
    'Country': 'Pais Venda',
    'City': 'Cidade Venda',
    'State': 'Estado Venda',
    'Postal Code': 'Codigo Postal Venda',
    'Region': 'Regiao Venda',
    'Product ID': 'ID Produto',
    'Category': 'Categoria Produto',
    'Sub-Category': 'Sub-Categoria Produto',
    'Product Name': 'Nome Produto',
    'Sales': 'Venda Total',
    'Quantity': 'Quantidade Vendida',
    'Discount': 'Desconto Aplicado',
    'Profit': 'Lucro Obtido'
}

# Tipos
colunas_tipos = {
    'Venda Total': 'float',
    'Desconto Aplicado': 'float',
    'Lucro Obtido': 'float',
    'Quantidade Vendida': 'int'
}

# Datas
colunas_datas = {
    'Data do Pedido': '%m/%d/%Y',
    'Data de Envio Pedido': '%m/%d/%Y'
}

# Caminho de saída
path_saida = 'data_processed/stores_sales_forecasting_tratado.csv'

# Pipeline
dados = Dados(path)

df_final = (
    dados
    .carregar_dados()
    .renomear_colunas(key_mapping)
    .converter_tipos(colunas_tipos, colunas_datas)
    .df
)

# Salvando
dados.salvar(path_saida)