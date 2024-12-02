import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho da pasta contendo os arquivos .xls
pasta = r"ds/União"

# Criar uma pasta para salvar os gráficos
output_dir = "plots/g1"
os.makedirs(output_dir, exist_ok=True)

# Carregar o arquivo
df = pd.read_csv(f'{pasta}/ingr_form.csv')
print(f"Arquivo carregado com sucesso: ingr_form.csv")

# --- Análise para cada dataset ---
# Substituir NaN por 0 nas colunas numéricas
df.fillna(0, inplace=True)

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
    data_by_sex = df.groupby('SEXO')[['INGRESSANTES', 'FORMADOS']].sum()
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

# Distribuição por sexo (geral)
data_by_sex = df_total.groupby('SEXO')[['INGRESSANTES', 'FORMADOS']].sum()
data_by_sex.plot(kind='bar', figsize=(8, 5), color=['skyblue', 'orange'])
plt.title('Distribuição de Ingressantes e Formados por Sexo (Geral)')
plt.xlabel('Sexo')
plt.ylabel('Quantidade')
plt.savefig(f"{output_dir}/Distribuicao_Sexo_Geral.png")
plt.close()

# --- Análise com Foco nos Top 10 Cursos ---
# Calcular o total de ingressantes e formados por curso
total_por_curso = df_total.groupby('COD_CURSO')[['INGRESSANTES', 'FORMADOS']].sum()

# Selecionar os 10 cursos com mais ingressantes
top_10_cursos = total_por_curso.sort_values(by='INGRESSANTES', ascending=False).head(10)

# --- Heatmap para os Top 10 Cursos ---
plt.figure(figsize=(20, 10))
sns.heatmap(top_10_cursos, annot=True, fmt=".0f", cmap="YlGnBu", cbar_kws={'label': 'Quantidade'})
plt.title('Top 10 Cursos com Mais Ingressantes e Formados')
plt.xlabel('Categoria')
plt.ylabel('Código do Curso')
plt.savefig(f"{output_dir}/Heatmap_Top10_Cursos.png")
plt.close()

# --- Taxa de Conclusão Geral para os Top 10 Cursos ---
# Calcular a taxa de conclusão (formados / ingressantes) para os Top 10 Cursos
top_10_cursos['TAXA_CONCLUSAO'] = (top_10_cursos['FORMADOS'] / top_10_cursos['INGRESSANTES']) * 100

# Ordenar os cursos por taxa de conclusão
top_10_cursos_sorted = top_10_cursos.sort_values(by='TAXA_CONCLUSAO', ascending=False)

# Gráfico de barras para a taxa de conclusão dos Top 10 Cursos
plt.figure(figsize=(20, 10))
sns.barplot(
    x=top_10_cursos_sorted.index,
    y=top_10_cursos_sorted['TAXA_CONCLUSAO'],
    palette="viridis",
    hue=top_10_cursos_sorted.index
)
plt.title('Taxa de Conclusão Geral (Top 10 Cursos)')
plt.xlabel('Código do Curso')
plt.ylabel('Taxa de Conclusão (%)')
plt.xticks(rotation=45)
plt.savefig(f"{output_dir}/Taxa_Conclusao_Top10_Cursos.png")
plt.close()
print(f"Análises gerais salvas em {output_dir}")
