import os
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt
import seaborn as sns
# Carregar dados
pasta_dados = 'ds/03_union'  
output_dir = 'plots/apriori'  
nome_arquivo = 'sit_turma.csv'
caminho_pasta = os.path.join(os.getcwd(), pasta_dados)
arquivo = os.path.join(caminho_pasta, nome_arquivo)
dados = pd.read_csv(arquivo)

# Criar as colunas binárias
dados['Aprovado'] = ((dados['%'] > 50) & (dados['Situação'] == 'Aprovado')).astype(int)
dados['Reprovado'] = ((dados['%'] > 50) & (dados['Situação'] == 'Reprovado')).astype(int)

# Transformar os outros atributos em colunas binárias
dados_binario = pd.get_dummies(dados[['Semestre', 'Cód. Disciplina']], prefix='', prefix_sep='')
dados_binario['Aprovado'] = dados['Aprovado']
dados_binario['Reprovado'] = dados['Reprovado']
dados_binario = dados_binario.astype(bool)

# Aplicar Apriori
itens_frequentes = apriori(dados_binario, min_support=0.001, use_colnames=True)
regras = association_rules(itens_frequentes, metric="confidence", min_threshold=0.1, num_itemsets=10)

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


regras_aprovacao['antecedents'] = regras_aprovacao['antecedents'].apply(lambda x: ', '.join(list(x)))
regras_aprovacao['consequents'] = regras_aprovacao['consequents'].apply(lambda x: ', '.join(list(x)))
heatmap_data = regras_aprovacao.pivot(index='antecedents', columns='consequents', values='support')

plt.figure(figsize=(10, 8)).subplots_adjust(left=0.2)
sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", fmt='.2f', cbar_kws={'label': 'Suporte'})
plt.title('Regras de Associação: Matriz de Calor')
plt.xlabel('Consequentes')
plt.ylabel('Antecedentes')
nome_grafico = f"{output_dir}/assoc_apro.png"
plt.savefig(nome_grafico)

regras_reprovacao['antecedents'] = regras_reprovacao['antecedents'].apply(lambda x: ', '.join(list(x)))
regras_reprovacao['consequents'] = regras_reprovacao['consequents'].apply(lambda x: ', '.join(list(x)))
heatmap_data = regras_reprovacao.pivot(index='antecedents', columns='consequents', values='support')

plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", fmt='.2f', cbar_kws={'label': 'Suporte'})
plt.title('Regras de Associação: Matriz de Calor')
plt.xlabel('Consequentes')
plt.ylabel('Antecedentes')
nome_grafico = f"{output_dir}/assoc_repro.png"
plt.savefig(nome_grafico)
