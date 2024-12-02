import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho da pasta contendo os arquivos .xlsx
pasta_dados = 'ds/União'

# Criar uma pasta para salvar os gráficos e arquivos de saída
output_dir = "plots/g3"
os.makedirs(output_dir, exist_ok=True)

# Processar cada arquivo .xlsx
caminho_arquivo = f'{pasta_dados}/sit_turma.csv'
df = pd.read_csv(caminho_arquivo)

# Agrupar os dados por Situação e somar os Alunos
df_agrupado = df.groupby(['Situação', 'Ano'])['%'].mean().reset_index()
plt.figure(figsize=(10, 8))
sns.lineplot(data=df_agrupado, x='Ano', y='%', hue='Situação', marker="*")
plt.title(f"Porcentagem de Alunos por Situação")
plt.xlabel('Ano')
plt.ylabel('Total de Alunos')
plt.xticks([2021,2022,2023], rotation=45)


nome_grafico = f"{output_dir}/Soma_Alunos_Situacao.png"
plt.savefig(nome_grafico)
plt.close()
print(f"Gráfico salvo em: {nome_grafico}")

print("Análise concluída.")
