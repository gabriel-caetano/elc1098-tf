import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho da pasta contendo os arquivos .xls
pasta = r"ds/original/Ingressantes e Formandos"

# Lista para armazenar os DataFrames
dataframes = []

# Criar uma pasta para salvar os gráficos
output_dir = "analises_graficas_c1"
os.makedirs(output_dir, exist_ok=True)

# Iterar sobre os arquivos na pasta
for arquivo in os.listdir(pasta):
    if arquivo.endswith('.xls'):  # Processar apenas arquivos .xls
        caminho_arquivo = os.path.join(pasta, arquivo)
        try:
            # Carregar o arquivo .xls
            df = pd.read_excel(caminho_arquivo, engine='xlrd')
            dataframes.append((arquivo, df))  # Armazenar o nome do arquivo e o DataFrame
            print(f"Arquivo carregado com sucesso: {arquivo}")

            # --- Análise para cada dataset ---
            # Substituir NaN por 0 nas colunas numéricas
            df.fillna(0, inplace=True)

            # Número de ingressantes e formados por ano
            data_by_year = df[df['ANO'] != 'TOTAL'].groupby('ANO')[['INGRESSANTES', 'FORMADOS']].sum()
            data_by_year.plot(kind='bar', figsize=(10, 6))
            plt.title(f'Ingressantes e Formados por Ano ({arquivo})')
            plt.xlabel('Ano')
            plt.ylabel('Quantidade')
            plt.savefig(f"{output_dir}/Ingressantes_Formados_Ano_{arquivo}.png")
            plt.close()

            # Distribuição por sexo
            data_by_sex = df.groupby('SEXO')[['INGRESSANTES', 'FORMADOS']].sum()
            data_by_sex.plot(kind='bar', figsize=(8, 5), color=['skyblue', 'orange'])
            plt.title(f'Distribuição de Ingressantes e Formados por Sexo ({arquivo})')
            plt.xlabel('Sexo')
            plt.ylabel('Quantidade')
            plt.savefig(f"{output_dir}/Distribuicao_Sexo_{arquivo}.png")
            plt.close()

        except Exception as e:
            print(f"Erro ao carregar o arquivo {arquivo}: {e}")

# --- Análise Geral com Todos os Dados ---
if dataframes:
    # Combinar todos os DataFrames
    df_combined = pd.concat([df for _, df in dataframes], ignore_index=True)

    # Filtrar apenas os dados com ANO == "TOTAL" para análises gerais
    df_total = df_combined[df_combined['ANO'] == 'TOTAL']
    
    # Número total de ingressantes e formados por ano
    data_by_year = df_combined.groupby('ANO')[['INGRESSANTES', 'FORMADOS']].sum()
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
        palette="viridis"
    )
    plt.title('Taxa de Conclusão Geral (Top 10 Cursos)')
    plt.xlabel('Código do Curso')
    plt.ylabel('Taxa de Conclusão (%)')
    plt.xticks(rotation=45)
    plt.savefig(f"{output_dir}/Taxa_Conclusao_Top10_Cursos.png")
    plt.close()

    # Salvar o dataset combinado
    df_combined.to_csv(f"{output_dir}/dados_combinados_c1.csv", index=False)
    print(f"Análises gerais salvas em {output_dir}")
