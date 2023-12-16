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
    df_dados.to_csv('dados_modificados.csv', sep='\t', index=False, header=None)


#%%
# Chamada da função com os nomes dos arquivos (ajuste conforme necessário)
substituir_codigos('codigos_capes.csv', 'br-capes-colsucup-prog-2021-2022-11-30.csv')


# %%
import pandas as pd
from datetime import datetime


# Substitua isso pelo caminho do seu arquivo CSV ou Excel
caminho_do_arquivo = 'dados_modificados.csv'

# Carregar apenas as 10 primeiras linhas do DataFrame
df_dados = pd.read_csv(caminho_do_arquivo, sep="\t",nrows=10)

# Filtrar o DataFrame
df_filtrado = df_dados[(df_dados['Situação do programa no ano de referência'] == 'EM FUNCIONAMENTO') & 
                (df_dados['Dependência administrativa da Instituição de Ensino Superior'] == 'PÚBLICA')]

# Função para criar o conteúdo do arquivo Markdown com Front Matter
def criar_markdown(linha):
    # Configuração do Front Matter
    front_matter = f"""---
layout: post
title: "{linha['Sigla da Instituição de Ensino Superior do programa de pós-graduação']} {linha['Nível do programa de pós-graduação']}: {linha['Nome do programa de pós-graduação']}"
date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
tags:
  -"{linha['Nome do programa de pós-graduação']}"
  -"{linha['Grande área do conhecimento do programa de pós-graduação']}"
  -"{linha['Sigla da Instituição de Ensino Superior do programa de pós-graduação']}"
  -"{linha['Grande Região onde está localizado o programa']}"
  -"{linha['Sigla da Unidade da Federação do programa']}"
  -"{linha['Município sede do programa de pós-graduação']}"
  -"{linha['Modalidade do programa de pós-graduação']}"
---

---

"""

    
    
    
    
    conteudo = f"""
# Informações sobre Programas de Pós-Graduação - Mestrados e Doutorados

## Visão Geral do Programa
- **Ano de Referência do Coleta:** {linha['Ano de referência do Coleta']}
- **Nome do Programa:** {linha['Nome do programa de pós-graduação']}
- **Nome em Inglês:** {linha['Nome do programa de pós-graduação em inglês']}
- **Nível do Programa:** {linha['Nível do programa de pós-graduação']}
- **Nota/Conceito:** {linha['Nota/Conceito do programa de pós-graduação']}
- **Ano de Início do Programa:** {linha['Ano de início do programa de pós-graduação']}
- **Situação Atual:** {linha['Situação do programa no ano de referência']}

## Instituição de Ensino
- **Sigla da Instituição:** {linha['Sigla da Instituição de Ensino Superior do programa de pós-graduação']}
- **Instituição de Ensino Superior:** {linha['Instituição de Ensino Superior do programa de pós-graduação']}
- **Código da Instituição na CAPES:** {linha['Código da Instituição de Ensino Superior na CAPES']}
- **Código e-Mec da Instituição:** {linha['Código e-Mec da Instituição de Ensino Superior']}
- **Status Jurídico:** {linha['Status Jurídico da Instituição de Ensino Superior']}
- **Dependência Administrativa:** {linha['Dependência administrativa da Instituição de Ensino Superior']}
- **Organização Acadêmica:** {linha['Organização acadêmica da Instituição de Ensino Superior']}

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

---

"""
    return front_matter + conteudo


# Diretório de destino para os arquivos Markdown
diretorio_destino = '../../_posts/'

# Criar um arquivo Markdown para cada linha do DataFrame filtrado
for index, linha in df_filtrado.iterrows():
    nome_arquivo = f"{diretorio_destino}{datetime.now().strftime('%Y-%m-%d')}_{linha['Sigla da Instituição de Ensino Superior do programa de pós-graduação']}_{linha['Nome do programa de pós-graduação']}.md"
    with open(nome_arquivo, 'w',encoding='utf-8') as arquivo:
        arquivo.write(criar_markdown(linha))

# %%
