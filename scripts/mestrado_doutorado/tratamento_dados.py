#%%

import pandas as pd

def substituir_codigos(nome_arquivo_codigos, nome_arquivo_dados):
    # Ler o primeiro arquivo com códigos e nomes legíveis
    df_codigos = pd.read_csv(nome_arquivo_codigos, sep='\t', usecols=[1, 2], header=None)
    mapeamento_codigos = dict(zip(df_codigos[1], df_codigos[2]))

    # Ler o segundo arquivo
    df_dados = pd.read_csv(nome_arquivo_dados, sep='\t', header=None)

    # Substituir os códigos na primeira linha pelos nomes legíveis
    df_dados.iloc[0] = df_dados.iloc[0].map(mapeamento_codigos)

    # Remover as três últimas colunas
    df_dados = df_dados.drop(df_dados.columns[-3:], axis=1)

    # Salvar o arquivo modificado
    df_dados.to_csv('mestrado_doutorado_univ_publicas.csv', sep='\t', index=False, header=None)


#%%
# Chamada da função com os nomes dos arquivos (ajuste conforme necessário)
substituir_codigos('codigos_capes.csv', 'br-capes-colsucup-prog-2021-2022-11-30.csv')


# %%
import pandas as pd
from datetime import datetime


# Substitua isso pelo caminho do seu arquivo CSV ou Excel
caminho_do_arquivo = 'mestrado_doutorado_univ_publicas.csv'

# Carregar apenas as 10 primeiras linhas do DataFrame
df_dados = pd.read_csv(caminho_do_arquivo, sep="\t" )#,nrows=100)

# Filtrar o DataFrame
df_filtrado = df_dados[(df_dados['Situação do programa no ano de referência'] == 'EM FUNCIONAMENTO') & 
                (df_dados['Dependência administrativa da Instituição de Ensino Superior'] == 'PÚBLICA')]

# Função para criar o conteúdo do arquivo Markdown com Front Matter
def criar_markdown(linha):
    # Configuração do Front Matter
    front_matter = f"""---
        layout: post
        title: "{linha['Nível do programa de pós-graduação']} em {linha['Nome do programa de pós-graduação']} na {linha['Sigla da Instituição de Ensino Superior do programa de pós-graduação']}  "
        date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
     
        tags:
        - {linha['Nível do programa de pós-graduação']}
        - "{linha['Nome do programa de pós-graduação'].replace(' ','-')}"
        - "{linha['Sigla da Instituição de Ensino Superior do programa de pós-graduação']}"
        - "{linha['Sigla da Unidade da Federação do programa']}"
        - CIDADE:{linha['Município sede do programa de pós-graduação'].replace(' ','-')}
        - NOTA:{linha['Nota/Conceito do programa de pós-graduação']}
        
       

        Nivel: "{linha['Nível do programa de pós-graduação']}"
        Nota: "{linha['Nota/Conceito do programa de pós-graduação']}"
        Instituicao: "{linha['Instituição de Ensino Superior do programa de pós-graduação']}"
        Estado: "{linha['Sigla da Unidade da Federação do programa']}"
        Area: "{linha['Área de conhecimento do programa de pós-graduação']}"
        
        
        
        
        
        \n---"""


    
    conteudo = f"""
## Visão Geral do Programa
- **Nome do Programa:** {linha['Nome do programa de pós-graduação']}
- **Nível:** {linha['Nível do programa de pós-graduação']}
- **Sigla da Instituição:** {linha['Sigla da Instituição de Ensino Superior do programa de pós-graduação']}
- **Instituição de Ensino Superior:** {linha['Instituição de Ensino Superior do programa de pós-graduação']}
- **Status Jurídico:** {linha['Status Jurídico da Instituição de Ensino Superior']}
- **Nota/Conceito:** {linha['Nota/Conceito do programa de pós-graduação']}
- **Ano de Início do Programa:** {linha['Ano de início do programa de pós-graduação']}
- **Ano de Referência do Coleta de dados:** {linha['Ano de referência do Coleta']}

## Localização do Programa
- **Grande Região:** {linha['Grande Região onde está localizado o programa']}
- **Sigla da Unidade da Federação:** {linha['Sigla da Unidade da Federação do programa']}
- **Município Sede:** {linha['Município sede do programa de pós-graduação']}

## Áreas de Conhecimento
- **Grande Área do Conhecimento:** {linha['Grande área do conhecimento do programa de pós-graduação']}
- **Área de Conhecimento:** {linha['Área de conhecimento do programa de pós-graduação']}
- **Área Básica do Conhecimento:** {linha['Área básica do conhecimento do programa de pós-graduação']}
- **Subárea:** {linha['Subárea do conhecimento do programa de pós-graduação']}
- **Especialidade:** {linha['Especialidade do conhecimento programa de pós-graduação']}

## Avaliação e Código do Programa
- **Código Identificador da Área de Avaliação:** {linha['Código identificador da área de avaliação do programa de pós-graduação']}
- **Área de Avaliação:** {linha['Área de avaliação do programa de pós-graduação']}
- **Código do Programa de Pós-Graduação:** {linha['Código do programa de pós-graduação']}


## Modalidade e Ano de Início do Curso
- **Modalidade do Programa:** {linha['Modalidade do programa de pós-graduação']}
- **Ano de Início de Cada Curso:** {linha['Ano de início de cada curso que compõe o programa']}
"""

    return front_matter + conteudo


# Diretório de destino para os arquivos Markdown
diretorio_destino = '../../_posts/'

# Criar um arquivo Markdown para cada linha do DataFrame filtrado
for index, linha in df_filtrado.iterrows():
    nome_arquivo = f"{diretorio_destino}{datetime.now().strftime('%Y-%m-%d')}-{linha['Sigla da Instituição de Ensino Superior do programa de pós-graduação']}-{linha['Nome do programa de pós-graduação']}.md"
    with open(nome_arquivo, 'w',encoding='utf-8') as arquivo:
        arquivo.write(criar_markdown(linha))

# %%
df_filtrado.to_csv("univ_filtradas.csv")
# %%
