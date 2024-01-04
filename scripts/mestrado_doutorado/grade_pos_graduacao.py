#%%
# Este arquivo cria a grade de exibição de cursos de mestrado e doutorado na página inicial 


import os
import yaml

# Definindo os itens base
base_items = [
    {
        "name": "Por instituição",
        "link": "pos-graduacao-instituicao",
        "image": "https://fakeimg.pl/300x100/0b71e6/fff/?text=Programas%20por%20Institui%C3%A7%C3%A3o&font=roboto",
        "description": "Navegue pelos programas de pós-graduação oferecidos por cada universidade pública brasileira. Encontre a instituição perfeita para você."
    },
    {
        "name": "Por estado",
        "link": "pos-graduacao-estado",
        "image": "https://fakeimg.pl/300x100/0b71e6/fff/?text=Programas%20por%20Estado&font=roboto",
        "description": "Busque programas de Mestrado e Doutorado por estado. Encontre instituições próximas e faça sua escolha com conveniência e proximidade."
    },
    {
        "name": "Por área",
        "link": "pos-graduacao-area",
        "image": "https://fakeimg.pl/300x100/0b71e6/fff/?text=Programas%20por%20%C3%81rea%20do%20conhecimento&font=roboto",
        "description": "Selecione programas de pós-graduação por área de interesse. Encontre o caminho ideal para avançar em sua área específica de estudo."
    },
    {
        "name": "Por classe",
        "link": "pos-graduacao-classe",
        "image": "https://fakeimg.pl/300x100/0b71e6/fff/?text=Programas%20por%20Classe&font=roboto",
        "description": "Lista de programas de mestrado e doutorado organizando por classe (Mestrado, Doutorado, Mestrado Profissional, etc.)"
    },
    {
        "name": "Por Nota Capes",
        "link": "pos-graduacao-nota",
        "image": "https://fakeimg.pl/300x100/0b71e6/fff/?text=Top%20CAPES&font=roboto",
        "description": "Descubra os programas com as melhores notas da CAPES. Escolha entre os mais bem avaliados para garantir uma educação de qualidade."
    }
]
# Regiões para as quais as entradas adicionais serão criadas
regions = ["CENTRO OESTE", "SUDESTE", "NORTE", "NORDESTE", "SUL"]

# Função para gerar as entradas YML
def generate_yml_entries(base_items, regions):
    yml_entries = []
    # Adicionando os itens base à lista
    yml_entries.extend(base_items)
    
    # Criando entradas para cada região adicional
    for region in regions:
        for item in base_items:
            # Copiando o item base e modificando para a região atual
            modified_item = item.copy()
            modified_item["name"] += f"/{region}"
            modified_item["link"] += f"-{region.lower().replace(' ', '-')}"
            # Alteração de cor na imagem para distinguir regiões
            modified_item["image"] = modified_item["image"].replace("0b71e6", "0b7100")
            yml_entries.append(modified_item)

    return yml_entries

# Gerando as entradas YML
yml_entries = generate_yml_entries(base_items, regions)

# Caminho do diretório onde o arquivo será salvo
save_directory = "../../_data"
os.makedirs(save_directory, exist_ok=True) # Cria o diretório se ele não existir

# Caminho do arquivo YML a ser gerado
yml_file_path = os.path.join(save_directory, "pos-graduacao.yml")

# Escrevendo as entradas no arquivo YML
with open(yml_file_path, 'w') as file:
    yaml.dump(yml_entries, file, default_flow_style=False, allow_unicode=True)

# Mensagem indicando sucesso
print("Arquivo 'pos-graduacao.yml' gerado com sucesso no diretório '../../_data'.")

# %%
