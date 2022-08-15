from IPython.display import display
import pandas as pd

info = {'valor': [120,200],
        'produto': ['A', 'B']
        }
info_df = pd.read_excel("Base Vendas.xlsx")

# display(info_df.head(20))
# print(info_df.shape)
# print(info_df.describe())

# produto = info_df[['Produto', 'Quantidade Vendida', 'Loja']]
# print(produto)

# print(info_df.loc[3:8])

# vendas_SP_df = (info_df.loc[info_df['Loja'] == 'São Paulo',['Loja','Produto','Quantidade Vendida']])
# print(vendas_SP_df)

# info_df['Teste'] = info_df['Preco Unitario'] / 100
# info_df = info_df.drop('Teste', axis = 1)

# info_df = info_df.dropna(how='all')

# vendas_estado = info_df['Loja'].value_counts()
# print(vendas_estado)

# vendas_produto = info_df.groupby('Produto').sum()
# print(vendas_produto)
