import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import  accuracy_score
import matplotlib.pyplot as plt

# Carregar dados
pasta_dados = 'ds/União'  
nome_arquivo = 'ingr_form.csv'
caminho_pasta = os.path.join(os.getcwd(), pasta_dados)
arquivo = os.path.join(caminho_pasta, nome_arquivo)
df = pd.read_csv(arquivo)

# Filtrando as linhas onde ANO não é 'TOTAL'
df_filtered = df[df['ANO'] != 'TOTAL']
# Convertendo a coluna 'ANO' para float
df_filtered['ANO'] = df_filtered['ANO'].astype(float)

# Agrupar os dados por 'CENTRO' e 'ANO' e somar os ingressantes para F e M
df_grouped = df_filtered.groupby(['CENTRO', 'ANO', 'SEXO'], as_index=False)['INGRESSANTES'].sum()

# Separando os ingressantes femininos (F) e masculinos (M)
df_feminino = df_grouped[df_grouped['SEXO'] == 'F'].rename(columns={'INGRESSANTES': 'F'})
df_masculino = df_grouped[df_grouped['SEXO'] == 'M'].rename(columns={'INGRESSANTES': 'M'})

# Fazendo o merge dos dados femininos e masculinos
df_final = pd.merge(df_feminino[['CENTRO', 'ANO', 'F']], df_masculino[['CENTRO', 'ANO', 'M']], on=['CENTRO', 'ANO'])

# Calculando as porcentagens de ingresso por sexo
df_final['PERCENTUAL_FEMININO'] = (df_final['F'] / (df_final['F'] + df_final['M'])) * 100
df_final['PERCENTUAL_MASCULINO'] = (df_final['M'] / (df_final['F'] + df_final['M'])) * 100

# Verificando o dataframe final
print(df_final.info())

# Codificando a variável 'CENTRO' como numérica (Label Encoding)
le = LabelEncoder()
df_final['CENTRO'] = le.fit_transform(df_final['CENTRO'])

# Dividindo os dados em variáveis independentes (X) e dependente (y)
X = df_final[['ANO', 'F', 'M', 'PERCENTUAL_FEMININO', 'PERCENTUAL_MASCULINO']]
y = df_final['CENTRO']

# Dividindo os dados em treino e teste (70% treino, 30% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criando o modelo de árvore de decisão
tree_model = DecisionTreeClassifier(random_state=42)

# Treinando o modelo
tree_model.fit(X_train, y_train)

# Realizando previsões no conjunto de teste
y_pred = tree_model.predict(X_test)

# Calculando a acurácia
accuracy = accuracy_score(y_test, y_pred)

# Imprimindo a acurácia
print(f"Acurácia do modelo de Árvore de Decisão: {accuracy * 100:.2f}%")

# Exemplo de previsão para novos dados
novo_ingressante = pd.DataFrame({
    'ANO': [2016],
    'F': [100],  # Exemplo de valor para F
    'M': [100],  # Exemplo de valor para M
    'PERCENTUAL_FEMININO': [30],  # Percentual feminino
    'PERCENTUAL_MASCULINO': [70]   # Percentual masculino
})

predicao = tree_model.predict(novo_ingressante)
print(f'O centro previsto para a entrada é: {le.inverse_transform(predicao)[0]}')


