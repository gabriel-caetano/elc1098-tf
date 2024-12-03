import os
import pandas as pd

# Caminho da pasta contendo os arquivos .xls
pasta = r"ds/União"

# Criar uma pasta para salvar os gráficos
output_dir = "ds/transform"
os.makedirs(output_dir, exist_ok=True)

# Carregar o arquivo
sit_turma = pd.read_csv(f'{pasta}/sit_turma.csv')
print(f"Arquivo carregado com sucesso: sit_turma.csv")

# Pivotado coluna situação em colunas com nr de aluno em cada situação
pivot = sit_turma.pivot_table(
    index=["Ano", "Semestre", "Cód. Disciplina", "Cód. Turma", "Professor", "Cód. Curso", "Curso"],
    columns=["Situação"],
    values=["Alunos", "%"],
    aggfunc="sum",
    fill_value=0  # Preenche valores ausentes com 0
)
pivot.columns = [
    "Aprovado%",
    "CancMatric%",
    "Dispensado%",
    "Não Concl.%",
    "Repr.Freq%",
    "Reprovado%",
    "Tr.Parcial%",
    "Aprovado",
    "CancMatric",
    "Dispensado",
    "Não Concl.",
    "Repr.Freq",
    "Reprovado",
    "Tr.Parcial"
]
pivot.reset_index().reset_index()
pivot["Total Alunos"] = pivot[
    ["Aprovado", "CancMatric", "Dispensado", "Não Concl.", "Repr.Freq", "Reprovado", "Tr.Parcial"]
].sum(axis=1)
pivot["Total %"] = pivot[
    ["Aprovado%", "CancMatric%", "Dispensado%", "Não Concl.%", "Repr.Freq%", "Reprovado%", "Tr.Parcial%"]
].sum(axis=1)
pivot.to_csv(f"{output_dir}/sit_turma.csv")
print(f"Arquivo salvo com sucesso: sit_turma.csv")

# transform ingr_form
ingr_form = pd.read_csv(f'{pasta}/ingr_form.csv')
print(f"Arquivo carregado com sucesso: ingr_form.csv")
# Remover NIVEL_CURSO
ingr_form = ingr_form.drop("NIVEL_CURSO", axis = 1)

# pivot ingressantes/formados por sexo
pivot = ingr_form.pivot_table(
    index=["COD_CURSO", "NOME_UNIDADE", "ANO", "CENTRO"],
    columns="SEXO",
    values=["INGRESSANTES","FORMADOS"],
    aggfunc="sum",
    fill_value=0
)
pivot.columns = ['INGRESSANTES_M', 'INGRESSANTES_F', 'FORMADOS_M', 'FORMADOS_F']
pivot = pivot.reset_index()
pivot["TOTAL_FORMADOS"] = pivot[["FORMADOS_M", "FORMADOS_F"]].sum(axis=1)
pivot["TOTAL_INGRESSANTES"] = pivot[["INGRESSANTES_M", "INGRESSANTES_F"]].sum(axis=1)
pivot["INGRESSANTES_M"] = pivot["INGRESSANTES_M"].astype(int)
pivot["INGRESSANTES_F"] = pivot["INGRESSANTES_F"].astype(int)
pivot["FORMADOS_M"] = pivot["FORMADOS_M"].astype(int)
pivot["FORMADOS_M"] = pivot["FORMADOS_M"].astype(int)
pivot["TOTAL_FORMADOS"] = pivot["TOTAL_FORMADOS"].astype(int)
pivot["TOTAL_INGRESSANTES"] = pivot["TOTAL_INGRESSANTES"].astype(int)
pivot["INGRESSANTES_M%"] = pivot["INGRESSANTES_M"]/pivot["TOTAL_INGRESSANTES"]
pivot["INGRESSANTES_F%"] = pivot["INGRESSANTES_F"]/pivot["TOTAL_INGRESSANTES"]
pivot["FORMADOS_M%"] = pivot["FORMADOS_M"]/pivot["TOTAL_FORMADOS"]
pivot["FORMADOS_F%"] = pivot["FORMADOS_F"]/pivot["TOTAL_FORMADOS"]

pivot.to_csv(f"{output_dir}/ingr_form.csv", index=False)
print(f"Arquivo salvo com sucesso: ingr_form.csv")

