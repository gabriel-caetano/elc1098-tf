import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Carregar dados
pasta_dados = 'ds/União'  
nome_arquivo = 'ingr_form.csv'
caminho_pasta = os.path.join(os.getcwd(), pasta_dados)
arquivo = os.path.join(caminho_pasta, nome_arquivo)
df = pd.read_csv(arquivo)

# Filtrando as linhas onde ANO não é 'TOTAL'
df_filtered = df[df['ANO'] != 'TOTAL']
df_filtered['ANO'] = df_filtered['ANO'].astype(float)

# Agrupar os dados por 'CENTRO' e 'ANO' e somar os ingressantes por sexo
df_grouped = df_filtered.groupby(['CENTRO', 'ANO', 'SEXO'], as_index=False)['INGRESSANTES'].sum()

# Pivotar para ter ingressantes F e M em colunas separadas
df_pivot = df_grouped.pivot_table(index=['CENTRO', 'ANO'], columns='SEXO', values='INGRESSANTES', fill_value=0).reset_index()

# Renomeando as colunas para F e M
df_pivot.rename(columns={'F': 'F', 'M': 'M'}, inplace=True)

# Criar a coluna TOTAL_INGRESSANTES e calcular percentual masculino
df_pivot['TOTAL_INGRESSANTES'] = df_pivot['F'] + df_pivot['M']
df_pivot['PERCENTUAL_MASCULINO'] = (df_pivot['M'] / df_pivot['TOTAL_INGRESSANTES']) * 100

# Remover as colunas F e M
df_final = df_pivot[['CENTRO', 'ANO', 'TOTAL_INGRESSANTES', 'PERCENTUAL_MASCULINO']]

# Codificando 'CENTRO' como numérica
le = LabelEncoder()
df_final['CENTRO'] = le.fit_transform(df_final['CENTRO'])

# Dividindo os dados
X = df_final[['ANO', 'TOTAL_INGRESSANTES', 'PERCENTUAL_MASCULINO']]
y = df_final['CENTRO']

# Separar em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=102)

# Modelo de árvore de decisão
tree_model = DecisionTreeClassifier(random_state=102)
tree_model.fit(X_train, y_train)

# Previsões e acurácia
y_pred = tree_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo de Árvore de Decisão: {accuracy * 100:.2f}%")
print(classification_report(y_test, y_pred))

# Exemplo de previsão para novos dados esperado que classique CT
novo_ingressante = pd.DataFrame({
    'ANO': [2016],
    'TOTAL_INGRESSANTES': [600],
    'PERCENTUAL_MASCULINO': [70]
})
predicao = tree_model.predict(novo_ingressante)
print(f'O centro previsto para a entrada 1 é: {le.inverse_transform(predicao)[0]}')

# Exemplo de previsão para novos dados esperado que classique CE
novo_ingressante = pd.DataFrame({
    'ANO': [2016],
    'TOTAL_INGRESSANTES': [900],
    'PERCENTUAL_MASCULINO': [20]
})
predicao = tree_model.predict(novo_ingressante)
print(f'O centro previsto para a entrada 2 é: {le.inverse_transform(predicao)[0]}')

# Exemplo de previsão para novos dados esperado que classique CCNE
novo_ingressante = pd.DataFrame({
    'ANO': [2016],
    'TOTAL_INGRESSANTES': [600],
    'PERCENTUAL_MASCULINO': [50]
})
predicao = tree_model.predict(novo_ingressante)
print(f'O centro previsto para a entrada 3 é: {le.inverse_transform(predicao)[0]}')

