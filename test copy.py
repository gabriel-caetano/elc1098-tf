import os
import pandas as pd

# Caminho da pasta contendo os arquivos .xls
pasta = r"ds/transform"

# Criar uma pasta para salvar os gráficos
output_dir = "ds/transform"
os.makedirs(output_dir, exist_ok=True)

# Carregar o arquivo
sit_turma = pd.read_csv(f'{pasta}/sit_turma.csv')
print(f"Arquivo carregado com sucesso: sit_turma.csv")

print(sit_turma[sit_turma["Total %"] == 100]['Total %'])
print(sit_turma[sit_turma["Total %"] != 100]["Total %"])
