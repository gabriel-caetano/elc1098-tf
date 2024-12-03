limpeza dos dados:
exclusão de arquvo duplicado
verificação do padrão das colunas
criação da coluna "CENTRO" para unir arquivos de ingressantes e formados
padronização dos nomes
conversão dos arquivos para csv
todo:
centralizar dados em 1 arquivo por estrutura

proposta de plotagem:
gráfico de aprov/reprov/reprov-freq x ano (3 linhas por cor)


original -> csv -> manual -> união -> plots -> 
                                   -> transformação -> limpeza
documentação:
- avaliação dos dados
- descrever problemas identificados
- - arquivos com formatos diferentes
- - Arquivo duplicado (CE)

- correções manuais realizadas
- - exclusão de arquivo duplicado (CE)

- descrever scripts criados para organizar os dados
- - padronizar arquivos como csv (convert_csv.py)
- - unir arquivos do mesmo formato (unir.py)
- - Transformar tabela de situação para ter uma coluna por situação com a quantidade de alunos em cada situação e uma coluna com o total de alunos


- identificar análises que podemos realizar
- - usar regressão na tabela de situação transformada para estimar a evolução da taxa de aprovação (% de alunos aprovados ou outras situações) por ano, prevendo anos futuros

- descrever scripts criados para realizar análises
