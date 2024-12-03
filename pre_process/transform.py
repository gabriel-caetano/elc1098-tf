import os
import pandas as pd

# Caminho da pasta contendo os arquivos .xls
pasta = r"ds/União"

# Criar uma pasta para salvar os gráficos
output_dir = "ds/transform"
os.makedirs(output_dir, exist_ok=True)

# Carregar o arquivo
df = pd.read_csv(f'{pasta}/sit_turma.csv')
print(f"Arquivo carregado com sucesso: sit_turma.csv")
pivot = df.pivot_table(
    index=["Ano", "Semestre", "Cód. Disciplina", "Cód. Turma", "Professor", "Cód. Curso", "Curso"],
    columns="Situação",
    values="Alunos",
    aggfunc="sum",
    fill_value=0  # Preenche valores ausentes com 0
)
pivot.to_csv(f"{output_dir}/sit_turma.csv")