# -*- coding: utf-8 -*-
"""Globalsolution.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ikvLZdOURqBCC7pcmUvrIr7AsUMMqk9P
"""

#Lucas Matheus da Silva - RM - 550466
#Arthur Pedroso de Francesco - RM - 551087

# Importar as bibliotecas necessárias
from sqlalchemy import create_engine
import pandas as pd

# Configurar a conexão com o banco de dados
# Substitua as informações abaixo pelos detalhes do seu banco de dados
database_type = '<global-solution>.mysql.database.azure.com'  # ex: 'postgresql'
username = 'fiap'
password = 'globalsolution2023'
host = 'global-solution.mysql.database.azure.com'
port = 'porta_do_servidor'
database_name = 'desperdicio'

# Criar a string de conexão
connection_string = f'{database_type}://{username}:{password}@{host}:{port}/{database_name}'

# Criar o objeto de conexão
engine = create_engine(connection_string)

# Consultar os produtos próximos ao vencimento
# Substitua 'tabela_produtos' pelo nome da tabela onde estão armazenados os produtos
# Substitua 'tabela_fornecedores' pelo nome da tabela onde estão armazenados os fornecedores
query = '''
SELECT p.nome AS produto, f.nome AS fornecedor
FROM tabela_produtos p
JOIN tabela_fornecedores f ON p.fornecedor_id = f.id
WHERE p.data_vencimento <= CURRENT_DATE()
'''

# Executar a consulta e obter os resultados em um DataFrame
df = pd.read_sql(query, engine)

# Exibir o resultado
df.head()
