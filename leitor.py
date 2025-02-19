import os
import random

# Função de troca de caracteres
def trocar_letras(texto):
    mapeamento = {
        'A': ['Ȧ', 'Ⱥ', 'Ḁ'],
        'E': ['Ё', 'Ḙ', 'Ě'],
        'I': ['Ĩ', 'Ḭ', 'İ'],
        'O': ['Ő', 'Ȫ', 'Ṍ'],
        'U': ['Ű', 'Ǜ', 'Ṳ'],
        'Y': ['Ẏ', 'Ŷ', 'Ÿ'],

        'a': ['ȧ', 'ӓ'],
        'e': ['ё', 'ě', 'ḙ'],
        'i': ['ḭ', 'ĩ', 'į'],
        'o': ['ọ', 'ȫ', 'ǫ'],
        'u': ['ũ', 'ṳ', 'ŭ'],
        'y': ['ŷ', 'ÿ', 'ẏ']
    }
    texto_modificado = ""
    for caractere in texto:
        if caractere in mapeamento:
            texto_modificado += random.choice(mapeamento[caractere])
        else:
            texto_modificado += caractere
    return texto_modificado

# Função principal
def copiar_arquivo():
    try:
        # Solicitar o caminho 
        caminho_original = input("Digite o caminho completo do arquivo .txt que deseja copiar: ")
        caminho_original = os.path.abspath(caminho_original) 

        if not os.path.exists(caminho_original):
            print("Erro: O arquivo especificado não foi encontrado.")
            return

        # Abrir o arquivo original para leitura
        with open(caminho_original, 'r', encoding='utf-8') as arquivo_original:
            conteudo = arquivo_original.read()

        # Substituir letras no conteúdo
        conteudo_modificado = trocar_letras(conteudo)

        caminho_copia = os.path.abspath(caminho_original)  

        # Criar o novo arquivo e escrever o conteúdo nele
        with open(caminho_copia, 'w', encoding='utf-8') as arquivo_copia:
            arquivo_copia.write(conteudo_modificado)

        print(f"Pronto")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Executar a função
copiar_arquivo()
