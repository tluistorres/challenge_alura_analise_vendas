import os

# Crie a pasta imagens se não existir
if not os.path.exists('imagens'):
    os.makedirs('imagens')

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os

# Crie a pasta imagens se não existir
if not os.path.exists('imagens'):
    os.makedirs('imagens')

# Crie uma conexão ao banco de dados
engine = create_engine('postgresql://postgres:torres0901@localhost:1024/postgres')

# Execute a consulta SQL e armazene os resultados em um DataFrame
df = pd.read_sql_query("""
    SELECT 'loja_1' AS loja, SUM(preco) AS faturamento
    FROM produtos
    WHERE ctid IN (
      SELECT ctid FROM produtos LIMIT 2359
    )
    UNION ALL
    SELECT 'loja_2' AS loja, SUM(preco) AS faturamento
    FROM produtos
    WHERE ctid IN (
      SELECT ctid FROM produtos OFFSET 2359 LIMIT 2359
    )
    UNION ALL
    SELECT 'loja_3' AS loja, SUM(preco) AS faturamento
    FROM produtos
    WHERE ctid IN (
      SELECT ctid FROM produtos OFFSET 4718 LIMIT 2359
    )
    UNION ALL
    SELECT 'loja_4' AS loja, SUM(preco) AS faturamento
    FROM produtos
    WHERE ctid IN (
      SELECT ctid FROM produtos OFFSET 7077
    );
""", engine)

# Crie um gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df['loja'], df['faturamento'])
plt.xlabel('Loja')
plt.ylabel('Faturamento')
plt.title('Faturamento das Lojas')

# Salve o gráfico como uma imagem
plt.savefig('imagens/faturamento_lojas.png', bbox_inches='tight')

# Exiba o gráfico
plt.show()
