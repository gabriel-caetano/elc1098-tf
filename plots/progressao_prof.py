import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho da pasta contendo os arquivos .xls
pasta = r"ds/clear"

# Criar uma pasta para salvar os gráficos
output_dir = "plots/progressao_prof"
os.makedirs(output_dir, exist_ok=True)

# Carregar o arquivo
sit_turma = pd.read_csv(f'{pasta}/sit_turma.csv')
print(f"Arquivo carregado com sucesso: sit_turma.csv")

def novo_ano(row):
    if row['Semestre'] == "1. Semestre":
        return row['Ano'] + 0.0
    elif row['Semestre'] == "2. Semestre":
        return row['Ano'] + 0.5
sit_turma["Outros%"] = sit_turma[["CancMatric%","Dispensado%","Não Concl.%","Repr.Freq%","Tr.Parcial%"]].sum(axis=1)
sit_turma["Ano"] = sit_turma.apply(novo_ano, axis=1)

professores = sit_turma['Professor'].unique()
anos = sit_turma['Ano'].unique()
sit_turma = sit_turma.groupby(['Professor', 'Ano'])[['Aprovado%', 'Reprovado%', 'Outros%']].mean().reset_index()
for professor in professores:
    dados_professor = sit_turma[sit_turma['Professor'] == professor]
    
    plt.figure(figsize=(10, 6))
    
    # Gráficos de linhas para cada situação
    plt.plot(dados_professor['Ano'], dados_professor['Aprovado%'], label='Aprovados%', marker='o')
    plt.plot(dados_professor['Ano'], dados_professor['Reprovado%'], label='Reprovados%', marker='o')
    plt.plot(dados_professor['Ano'], dados_professor['Outros%'], label='Outros%', marker='o')
    
    # Personalização do gráfico
    plt.title(f'Desempenho por Ano - Professor {professor}')
    plt.xlabel('Ano')
    plt.ylabel('Porcentagem (%)')
    plt.xticks(ticks=anos, labels=anos)
    
    # Mostrar o gráfico
    nome_grafico = f"{output_dir}/progr_prof_{professor}.png"
    plt.savefig(nome_grafico)
    plt.close()
# centro_counts = merged_data.groupby('CENTRO').size().reset_index(name='Quantidade')
# print(centro_counts)
# sns.barplot(data=centro_counts, x='CENTRO', y='Quantidade')
# nome_grafico = f"{output_dir}/qtd_por_centro.png"
# plt.savefig(nome_grafico)
# ct_data =  merged_data[merged_data["CENTRO"] == 'CT'] # 130

# performance_data = ct_data.groupby('Curso').agg({
#     'Aprovado%': 'mean',
#     'Reprovado%': 'mean',
#     'Outros%': 'mean',
#     'FORMADOS_M%': 'mean',
#     'FORMADOS_F%': 'mean'
# }).reset_index().sort_values(by='Aprovado%', ascending=False)
# plt.figure(figsize=(15, 8)).subplots_adjust(left=0.3)
# sns.barplot(data=performance_data, x='Aprovado%', y='Curso')
# plt.title(f"Aprovação por curso")
# plt.xlabel('% Aprovação')
# plt.ylabel('Curso')
# nome_grafico = f"{output_dir}/aprovacao_curso.png"
# plt.savefig(nome_grafico)
# plt.close()

# performance_data = merged_data.groupby('CENTRO').agg({
#     'Aprovado%': 'mean',
#     'Reprovado%': 'mean',
#     'Outros%': 'mean',
#     'FORMADOS_M%': 'mean',
#     'FORMADOS_F%': 'mean'
# }).reset_index().sort_values(by='Aprovado%', ascending=False)

# plt.figure(figsize=(15, 8)).subplots_adjust(left=0.3)
# sns.barplot(data=performance_data, x='Aprovado%', y='CENTRO')
# plt.title(f"Aprovação por centro")
# plt.xlabel('% Aprovação')
# plt.ylabel('Centro')
# nome_grafico = f"{output_dir}/aprovacao_centro.png"
# plt.savefig(nome_grafico)
# plt.close()

# professor_performance = sit_turma.groupby('Professor').agg({
#     'Aprovado%': 'mean',
#     'Reprovado%': 'mean',
#     'Outros%': 'mean'
# }).reset_index().sort_values(by='Reprovado%', ascending=False)
# print(professor_performance.sort_values(by='Reprovado%', ascending=False))

# professor_performance = sit_turma.groupby('Professor')[['Aprovado%',
#     'Reprovado%',
#     'Outros%']].mean().sort_values(by='Aprovado%', ascending=False)
# professor_performance.plot(kind='barh', figsize=(9, 12), color=['green', 'red', 'blue'], left=0.3)
# plt.title(f'Taxa de aprovação, reprovação e outros por professor')
# plt.ylabel('Professor')
# plt.xlabel('Taxa')
# plt.savefig(f"{output_dir}/taxa_professor.png")
# plt.close()