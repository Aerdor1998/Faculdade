# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gA1BswMoIscdKygVXqIFmHJo4mpj2dpx
"""

import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal

config = {
  'host':'<global-solution>.mysql.database.azure.com',
  'user':'<fiap>',
  'password':'<globalsolution2023>', #ou fiap2023
  'database':'<despedicio>'
}

# Construct connection string

try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

# Drop previous table of same name if one exists
cursor.execute("DROP TABLE IF EXISTS inventory;")
print("Finished dropping table (if existed).")

# Create table
cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
print("Finished creating table.")

# Insert some data into table
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
print("Inserted",cursor.rowcount,"row(s) of data.")
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
print("Inserted",cursor.rowcount,"row(s) of data.")
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
print("Inserted",cursor.rowcount,"row(s) of data.")
import pandas as pd
from datetime import date, timedelta

# Dados de exemplo para produtos
produtos = [
    {"Produto": "Maçã", "Fornecedor": "Fornecedor A", "Data_Vencimento": date(2023, 6, 20)},
    {"Produto": "Banana", "Fornecedor": "Fornecedor B", "Data_Vencimento": date(2023, 6, 18)},
    {"Produto": "Abacaxi", "Fornecedor": "Fornecedor C", "Data_Vencimento": date(2023, 6, 22)},
    {"Produto": "Melancia", "Fornecedor": "Fornecedor D", "Data_Vencimento": date(2023, 6, 21)},
    {"Produto": "Laranja", "Fornecedor": "Fornecedor E", "Data_Vencimento": date(2023, 6, 19)},
    {"Produto": "Pera", "Fornecedor": "Fornecedor F", "Data_Vencimento": date(2023, 6, 23)},
    {"Produto": "Manga", "Fornecedor": "Fornecedor G", "Data_Vencimento": date(2023, 6, 25)},
    {"Produto": "Uva", "Fornecedor": "Fornecedor H", "Data_Vencimento": date(2023, 6, 24)},
    {"Produto": "Morango", "Fornecedor": "Fornecedor I", "Data_Vencimento": date(2023, 6, 27)},
    {"Produto": "Kiwi", "Fornecedor": "Fornecedor J", "Data_Vencimento": date(2023, 6, 26)}
]

# Criar o DataFrame
data = pd.DataFrame(produtos)

# Exibir o DataFrame
print(data)

# Cleanup
conn.commit()
cursor.close()
conn.close()
print("Done.")