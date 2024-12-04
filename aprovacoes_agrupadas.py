import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho da pasta contendo os arquivos .xls
pasta = r"ds/clear"

# Criar uma pasta para salvar os gráficos
output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

# Carregar o arquivo
sit_turma = pd.read_csv(f'{pasta}/sit_turma.csv')
print(f"Arquivo carregado com sucesso: sit_turma.csv")
ingr_form = pd.read_csv(f'{pasta}/ingr_form.csv')
print(f"Arquivo carregado com sucesso: ingr_form.csv")

ingr_form["COD_CURSO"] = ingr_form["COD_CURSO"].astype(str)
sit_turma["Cód. Curso"] = sit_turma["Cód. Curso"].astype(str)
ingr_form["ANO"] = ingr_form["ANO"].astype(str)
sit_turma["Ano"] = sit_turma["Ano"].astype(str)
sit_turma["Outros%"] = sit_turma[["CancMatric%","Dispensado%","Não Concl.%","Repr.Freq%","Tr.Parcial%"]].sum(axis=1)


merged_data = pd.merge(ingr_form, sit_turma, left_on=["COD_CURSO", "ANO"], right_on=["Cód. Curso", "Ano"])

centro_counts = merged_data.groupby('CENTRO').size().reset_index(name='Quantidade')
print(centro_counts)
sns.barplot(data=centro_counts, x='CENTRO', y='Quantidade')
nome_grafico = f"{output_dir}/qtd_por_centro.png"
plt.savefig(nome_grafico)

performance_data = merged_data.groupby('Curso').agg({
    'Aprovado%': 'mean',
    'Reprovado%': 'mean',
    'Outros%': 'mean',
    'FORMADOS_M%': 'mean',
    'FORMADOS_F%': 'mean'
}).reset_index().sort_values(by='Aprovado%', ascending=False)
plt.figure(figsize=(15, 8)).subplots_adjust(left=0.3)
sns.barplot(data=performance_data, x='Aprovado%', y='Curso')
plt.title(f"Aprovação por curso")
plt.xlabel('% Aprovação')
plt.ylabel('Curso')
nome_grafico = f"{output_dir}/aprovacao_curso.png"
plt.savefig(nome_grafico)
plt.close()

plt.figure(figsize=(15, 8)).subplots_adjust(left=0.3)
sns.barplot(data=performance_data.sort_values(by='Reprovado%', ascending=False), x='Reprovado%', y='Curso')
plt.title(f"Reprovação por curso")
plt.xlabel('% Reprovação')
plt.ylabel('Curso')
nome_grafico = f"{output_dir}/reprovacao_curso.png"
plt.savefig(nome_grafico)
plt.close()

plt.figure(figsize=(15, 8)).subplots_adjust(left=0.3)
sns.barplot(data=performance_data.sort_values(by='Outros%', ascending=False), x='Outros%', y='Curso')
plt.title(f"Outros por curso")
plt.xlabel('% Outros')
plt.ylabel('Curso')
nome_grafico = f"{output_dir}/outros_curso.png"
plt.savefig(nome_grafico)
plt.close()


performance_data = merged_data.groupby('CENTRO').agg({
    'Aprovado%': 'mean',
    'Reprovado%': 'mean',
    'Outros%': 'mean',
    'FORMADOS_M%': 'mean',
    'FORMADOS_F%': 'mean'
}).reset_index().sort_values(by='Aprovado%', ascending=False)

plt.figure(figsize=(15, 8))
sns.barplot(data=performance_data, x='Aprovado%', y='CENTRO')
plt.title(f"Aprovação por centro")
plt.xlabel('% Aprovação')
plt.ylabel('Centro')
nome_grafico = f"{output_dir}/aprovacao_centro.png"
plt.savefig(nome_grafico)
plt.close()

plt.figure(figsize=(15, 8))
sns.barplot(data=performance_data.sort_values(by='Reprovado%', ascending=False), x='Reprovado%', y='CENTRO')
plt.title(f"Reprovação por centro")
plt.xlabel('% Reprovação')
plt.ylabel('Centro')
nome_grafico = f"{output_dir}/reprovacao_centro.png"
plt.savefig(nome_grafico)
plt.close()

plt.figure(figsize=(15, 8))
sns.barplot(data=performance_data.sort_values(by='Outros%', ascending=False), x='Outros%', y='CENTRO')
plt.title(f"Outros por centro")
plt.xlabel('% Outros')
plt.ylabel('Centro')
nome_grafico = f"{output_dir}/outros_centro.png"
plt.savefig(nome_grafico)
plt.close()