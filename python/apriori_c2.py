import os
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Carregar dados
pasta_dados = 'analises_graficas_c2'  
nome_arquivo = 'dados_gerais.xlsx'
caminho_pasta = os.path.join(os.getcwd(), pasta_dados)
arquivo = os.path.join(caminho_pasta, nome_arquivo)
dados = pd.read_excel(arquivo, engine='openpyxl')

# Criar as colunas binárias
dados['Aprovado'] = ((dados['%'] > 50) & (dados['Situação'] == 'Aprovado')).astype(int)
dados['Reprovado'] = ((dados['%'] > 50) & (dados['Situação'] == 'Reprovado')).astype(int)

# Transformar os outros atributos em colunas binárias
# Da pra explorar mais colunas aqui talvez... Não testei
dados_binario = pd.get_dummies(dados[['Semestre', 'Cód. Disciplina']], prefix='', prefix_sep='')
dados_binario['Aprovado'] = dados['Aprovado']
dados_binario['Reprovado'] = dados['Reprovado']
dados_binario = dados_binario.astype(int)

# Aplicar Apriori
itens_frequentes = apriori(dados_binario, min_support=0.001, use_colnames=True)
regras = association_rules(itens_frequentes, metric="confidence", min_threshold=0.1)

# Selecionar saida de regras resumida e organizada
regras['count'] = regras['support'] * len(dados_binario)
regras = regras[['antecedents', 'consequents', 'support', 'confidence', 'lift', 'count']]
regras = regras.sort_values(by='confidence', ascending=False)

# Filtrar regras relacionadas à Reprovação
regras_reprovacao = regras[regras['consequents'].apply(lambda x: 'Reprovado' in list(x))]
print("\nRegras relacionadas à Reprovação:")
print(regras_reprovacao)

# Filtrar regras relacionadas à Aprovação
regras_aprovacao = regras[regras['consequents'].apply(lambda x: 'Aprovado' in list(x))]
print("\nRegras relacionadas à Aprovação:")
print(regras_aprovacao)