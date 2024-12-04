import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho da pasta contendo os arquivos .xls
pasta = r"ds/03_union"

# Criar uma pasta para salvar os gráficos
output_dir = "plots/ingr_form_view"
os.makedirs(output_dir, exist_ok=True)

# Carregar o arquivo
df = pd.read_csv(f'{pasta}/ingr_form.csv')
print(f"Arquivo carregado com sucesso: ingr_form.csv")

centros = list(set(df["CENTRO"]))
for centro in centros:
    # Número de ingressantes e formados por ano
    centro_df = df[df['CENTRO'] == centro]
    data_by_year = centro_df[centro_df['ANO'] != 'TOTAL'].groupby('ANO')[['INGRESSANTES', 'FORMADOS']].sum()
    data_by_year.plot(kind='bar', figsize=(10, 6))
    plt.title(f'Ingressantes e Formados por Ano ({centro})')
    plt.xlabel('Ano')
    plt.ylabel('Quantidade')
    plt.savefig(f"{output_dir}/Ingressantes_Formados_Ano_{centro}.png")
    plt.close()
    print(f"salvo Ingressantes_Formados_Ano_{centro}.png")

    # Distribuição por sexo
    data_by_sex = centro_df.groupby('SEXO')[['INGRESSANTES', 'FORMADOS']].sum()
    data_by_sex.plot(kind='bar', figsize=(8, 5), color=['skyblue', 'orange'])
    plt.title(f'Distribuição de Ingressantes e Formados por Sexo ({centro})')
    plt.xlabel('Sexo')
    plt.ylabel('Quantidade')
    plt.savefig(f"{output_dir}/Distribuicao_Sexo_{centro}.png")
    plt.close()
    print(f"salvo Distribuicao_Sexo_{centro}.png")

# Filtrar apenas os dados com ANO == "TOTAL" para análises gerais
df_total = df[df['ANO'] == 'TOTAL']
    
# Número total de ingressantes e formados por ano
data_by_year = df.groupby('ANO')[['INGRESSANTES', 'FORMADOS']].sum()
data_by_year.plot(kind='bar', figsize=(10, 6))
plt.title('Ingressantes e Formados por Ano (Geral)')
plt.xlabel('Ano')
plt.ylabel('Quantidade')
plt.savefig(f"{output_dir}/Ingressantes_Formados_Ano_Geral.png")
plt.close()

print(f"Análises gerais salvas em {output_dir}")
