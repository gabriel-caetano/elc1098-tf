import os
import pandas as pd

# Caminho da pasta contendo os arquivos .xls
pasta = r"ds/04_transform"

# Criar uma pasta para salvar os gráficos
output_dir = "ds/05_clear"
os.makedirs(output_dir, exist_ok=True)

# Carregar o arquivo
sit_turma = pd.read_csv(f'{pasta}/sit_turma.csv')
print(f"Arquivo carregado com sucesso: sit_turma.csv")

# get only completed values
sit_turma = sit_turma[sit_turma["Total %"] >= 95]

sit_turma.to_csv(f"{output_dir}/sit_turma.csv", index=False)

pd.read_csv(f'{pasta}/ingr_form.csv').to_csv(f"{output_dir}/ingr_form.csv", index=False)