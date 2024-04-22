import re

# INDEXAÇÃO DO TEXTO ---------------------------------------------------------------------------------------------------
def extract_modules_txt(texto):
    """
        Extrai os módulos e seus detalhes do texto.

        Args:
            texto (str): O texto do qual os módulos serão extraídos.

        Returns:
            dict: Um dicionário onde as chaves são os nomes dos módulos e os valores são os detalhes dos módulos.
        """
    modulos = {}
    padrao_modulo = re.compile(r'\d+-\s*(\w+)', re.IGNORECASE)
    matches = padrao_modulo.finditer(texto)

    for match in matches:
        nome_modulo = match.group(1).upper()
        inicio_modulo = match.start()
        fim_modulo = len(texto)

        if match.end():
            fim_modulo = match.end()

        detalhes_modulo = texto[inicio_modulo:fim_modulo]
        modulos[nome_modulo] = detalhes_modulo

    return modulos


# Função para imprimir os detalhes de cada módulo
def print_details_modules_txt(modulos):
    """
        Imprime os detalhes de cada módulo.

        Args:
            modulos (dict): Um dicionário onde as chaves são os nomes dos módulos e os valores são os detalhes dos módulos.

        Returns:
            None
        """
    for nome, detalhes in modulos.items():
        print(f"Módulo: {nome}")
        print(detalhes)
        print("-" * 50)


# Caminho do arquivo
txt_path = r'C:/Projects/PESSOAL/aiEngineeringChallenge/challenge-artificial-intelligence/resources/modulos_aprendizagem_gerados_chatGPT'

# Ler o conteúdo do arquivo
with open(txt_path, 'r', encoding='utf-8') as f:
    file_text = f.read()

# Extrair os módulos e seus detalhes
module = extract_modules_txt(file_text)

# Imprimir os detalhes dos módulos
print_details_modules_txt(module)


# INDEXAÇÃO DO PDF -----------------------------------------------------------------------------------------------------

# INDEXAÇÃO DO MP4 -----------------------------------------------------------------------------------------------------

