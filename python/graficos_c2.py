import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho da pasta contendo os arquivos .xlsx -- MUDAR AQUI QUANDO FOR TESTAR
pasta = r"C:\Users\bruno\OneDrive\Área de Trabalho\elc1098-tf-main\ds"

# Lista para armazenar os DataFrames
dataframes = []

# Criar uma pasta para salvar os gráficos
output_dir = "analises_graficas_c2"
os.makedirs(output_dir, exist_ok=True)

# Iterar sobre os arquivos na pasta
for arquivo in os.listdir(pasta):
    if arquivo.endswith('.xlsx'):  # Processar apenas arquivos .xlsx
        caminho_arquivo = os.path.join(pasta, arquivo)
        try:
            # Carregar o arquivo .xlsx usando a engine 'openpyxl'
            df = pd.read_excel(caminho_arquivo, engine='openpyxl')
            dataframes.append((arquivo, df))  # Armazenar o nome do arquivo e o DataFrame
            print(f"Arquivo carregado com sucesso: {arquivo}")

            # --- Análise para cada dataset ---
            # Substituir NaN por 0 nas colunas numéricas
            df.fillna(0, inplace=True)
            #print(df.info())

            # Distribuição de alunos por situação
            plt.figure(figsize=(10, 6))
            sns.countplot(data=df, x='Situação', hue='Situação', palette='Set2', legend=False)
            plt.title(f"Distribuição de Alunos por Situação ({arquivo})")
            plt.xlabel('Situação')
            plt.ylabel('Número de Alunos')
            plt.savefig(f"{output_dir}/Distribuicao_Situacao_{arquivo}.png")
            plt.close()

            # Distribuição de alunos por semestre (considerando 'Ano' e 'Semestre')
            plt.figure(figsize=(10, 6))
            sns.countplot(data=df, x='Semestre', hue='Ano', palette='viridis', legend=False)
            plt.title(f"Distribuição de Alunos por Semestre ({arquivo})")
            plt.xlabel('Semestre')
            plt.ylabel('Número de Alunos')
            plt.savefig(f"{output_dir}/Distribuicao_Semestre_{arquivo}.png")
            plt.close()

            # DA PRA ANALISAR MAIS TAMBÉM AQUI

        except Exception as e:
            print(f"Erro ao carregar o arquivo {arquivo}: {e}")

# --- Análise Geral com Todos os Dados --- FAZER AINDA
if dataframes:
    # Combinar todos os DataFrames
    df_combined = pd.concat([df for _, df in dataframes], ignore_index=True)

    #print(df_combined.info())

    # Salvar o dataset combinado
    output_combined_path = os.path.join(output_dir, 'dados_combinados_c2.xlsx')
    df_combined.to_excel(output_combined_path, index=False, engine='openpyxl')
    print(f"DataFrame combinado salvo em: {output_combined_path}")

