import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho da pasta contendo os arquivos .xlsx
pasta_dados = 'ds'
caminho_pasta = os.path.join(os.getcwd(), pasta_dados)

# Criar uma pasta para salvar os gráficos e arquivos de saída
output_dir = "analises_graficas_c2"
os.makedirs(output_dir, exist_ok=True)

dataframes = []

# Processar cada arquivo .xlsx
for arquivo in os.listdir(caminho_pasta):
    if arquivo.endswith('.xlsx'):  
        caminho_arquivo = os.path.join(caminho_pasta, arquivo)
        try:
            df = pd.read_excel(caminho_arquivo, engine='openpyxl')
            print(f"Arquivo carregado com sucesso: {arquivo}")

            dataframes.append(df)

            # Agrupar os dados por Situação e somar os Alunos
            df_agrupado = df.groupby('Situação')['Alunos'].sum().reset_index()

            plt.figure(figsize=(10, 6))
            sns.barplot(data=df_agrupado, x='Situação', y='Alunos', hue='Situação', palette='Set2', dodge=False, legend=False)
            plt.title(f"Soma de Alunos por Situação ({arquivo})")
            plt.xlabel('Situação')
            plt.ylabel('Total de Alunos')
            plt.xticks(rotation=45)

            nome_grafico = f"{output_dir}/Soma_Alunos_Situacao_{os.path.splitext(arquivo)[0]}.png"
            plt.savefig(nome_grafico)
            plt.close()
            print(f"Gráfico salvo em: {nome_grafico}")

        except Exception as e:
            print(f"Erro ao processar o arquivo {arquivo}: {e}")

# Criar arquivos com dados gerais
if dataframes:
    df_geral = pd.concat(dataframes, ignore_index=True)

    caminho_tabela_geral = os.path.join(output_dir, 'dados_gerais.xlsx')
    df_geral.to_excel(caminho_tabela_geral, index=False, engine='openpyxl')
    print(f"Arquivo geral com todos os dados concatenados salvo em: {caminho_tabela_geral}")

    estatisticas = df_geral.groupby('Situação')['Alunos'].agg(
        Total='sum',
        Média='mean',
        Mediana='median',
        Desvio_Padrão='std',
        Ocorrências='count'
    ).reset_index()

    caminho_tabela_estatistica = os.path.join(output_dir, 'estatisticas_detalhadas.xlsx')
    estatisticas.to_excel(caminho_tabela_estatistica, index=False, engine='openpyxl')
    print(f"Tabela de estatísticas detalhadas salva em: {caminho_tabela_estatistica}")

    plt.figure(figsize=(10, 6))
    sns.barplot(data=estatisticas, x='Situação', y='Total', hue='Situação', palette='muted', dodge=False, legend=False)
    plt.title("Soma Geral de Alunos por Situação")
    plt.xlabel('Situação')
    plt.ylabel('Total de Alunos')
    plt.xticks(rotation=45)

    caminho_grafico_geral = os.path.join(output_dir, 'Soma_Geral_Alunos_Situacao.png')
    plt.savefig(caminho_grafico_geral)
    plt.close()
    print(f"Gráfico geral salvo em: {caminho_grafico_geral}")

print("Análise concluída.")
