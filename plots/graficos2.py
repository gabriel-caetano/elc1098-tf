import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho da pasta contendo os arquivos .xlsx
pasta_dados = 'ds/União'
# Criar uma pasta para salvar os gráficos e arquivos de saída
output_dir = "plots/g2"
os.makedirs(output_dir, exist_ok=True)

# Processar cada centro
df = pd.read_csv(f"{pasta_dados}/sit_turma.csv")
print(f"Arquivo carregado com sucesso: sit_turma.csv")
disciplinas = list(set(df["Cód. Disciplina"]))
anos = list(set(df["Ano"]))
for disc in disciplinas:
    for ano in anos:
        sub_df = df[df["Ano"] == ano][df["Cód. Disciplina"] == disc]
        if sub_df.empty:
            break
        df_agrupado = sub_df.groupby('Situação')['Alunos'].sum().reset_index()
        plt.figure(figsize=(10, 6))
        sns.barplot(data=df_agrupado, x='Situação', y='Alunos', hue='Situação', palette='Set2', dodge=False, legend=False)
        plt.title(f"Soma de Alunos por Situação ({disc}, {ano})")
        plt.xlabel('Situação')
        plt.ylabel('Total de Alunos')
        plt.xticks(rotation=45)

        nome_grafico = f"{output_dir}/Soma_Alunos_Situacao_{disc}_{ano}.png"
        plt.savefig(nome_grafico)
        plt.close()
        print(f"Gráfico salvo em: {nome_grafico}")
print(disciplinas)

# Criar arquivos com dados gerais
estatisticas = df.groupby('Situação')['Alunos'].agg(
    Total='sum',
    Média='mean',
    Mediana='median',
    Desvio_Padrão='std',
    Ocorrências='count'
).reset_index()

caminho_tabela_estatistica = os.path.join(output_dir, 'estatisticas_detalhadas.csv')
estatisticas.to_csv(caminho_tabela_estatistica, index=False)
print(f"Tabela de estatísticas detalhadas salva em: {caminho_tabela_estatistica}")

plt.figure(figsize=(10, 6))
sns.barplot(data=estatisticas, x='Situação', y='Total', hue='Situação', palette='muted', dodge=False, legend=False)
plt.title("Soma Geral de Alunos por Situação")
plt.xlabel('Situação')
plt.ylabel('Total de Alunos')
plt.xticks(rotation=45)

caminho_grafico_geral = os.path.join(output_dir, 'Soma_Geral_Alunos_Situacao.png')
plt.savefig(caminho_grafico_geral)
plt.close()
print(f"Gráfico geral salvo em: {caminho_grafico_geral}")

print("Análise concluída.")
