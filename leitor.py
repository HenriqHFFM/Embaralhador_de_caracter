import os
import random

# Função de troca de caracteres
def trocar_letras(texto):
    mapeamento = {
        'A': ['Ȧ', 'Ⱥ', 'Ḁ'],
        'B': ['В', 'Ḅ', 'Ɓ'],
        'C': ['Ƈ', 'Ć', 'Č'],
        'D': ['Ḑ', 'Ḓ', 'Ɖ'],
        'E': ['Ё', 'Ḙ', 'Ě'],
        'F': ['Ḟ', 'Ƒ'],
        'G': ['Ġ', 'Ḡ'],
        'H': ['Ȟ', 'Ḥ'],
        'I': ['Ĩ', 'Ḭ', 'İ'],
        'J': ['Ĵ', 'ǰ'],
        'K': ['Ǩ', 'Ḱ', 'Ḳ'],
        'L': ['Ḷ', 'Ḻ'],
        'M': ['Ḿ', 'Ṁ'],
        'N': ['Ṅ', 'Ň', 'Ɲ'],
        'O': ['Ő', 'Ȫ', 'Ṍ'],
        'P': ['Ṕ', 'Ṗ', 'Ƥ'],
        'Q': ['Ꝗ', 'Ꝙ'],
        'R': ['Ȑ', 'Ṙ', 'Ŕ'],
        'S': ['Ș', 'Ṡ'],
        'T': ['Ț', 'Ṫ'],
        'U': ['Ű', 'Ǜ', 'Ṳ'],
        'V': ['Ṽ', 'Ṿ', 'Ʋ'],
        'W': ['Ẃ', 'Ẅ', 'Ŵ'],
        'X': ['Ẍ', 'Х'],
        'Y': ['Ẏ', 'Ŷ', 'Ÿ'],
        'Z': ['Ż', 'Ẑ', 'Ƶ'],

        'a': ['ȧ', 'ӓ'],
        'b': ['ƀ', 'ƃ', 'ḅ'],
        'c': ['ċ', 'č', 'ç'],
        'd': ['ḓ', 'ḑ', 'đ'],
        'e': ['ё', 'ě', 'ḙ'],
        'f': ['ƒ', 'ḟ', 'ᵮ'],
        'g': ['ĝ', 'ġ', 'ģ'],
        'h': ['ḩ', 'ḥ', 'ĥ'],
        'i': ['ḭ', 'ĩ', 'į'],
        'j': ['ĵ', 'ʝ', 'ǰ'],
        'k': ['ķ', 'ḱ', 'ǩ'],
        'l': ['ḷ', 'ł', 'ŀ'],
        'm': ['ṁ', 'ṃ', 'ᵯ'],
        'n': ['ṅ', 'ň', 'ñ'],
        'o': ['ọ', 'ȫ', 'ǫ'],
        'p': ['ṕ', 'ṗ'],
        'q': ['ɋ', 'ꝗ'],
        'r': ['ŕ', 'ṙ', 'ȑ'],
        's': ['ṣ', 'ś', 'š'],
        't': ['ṭ', 'ț', 'ŧ'],
        'u': ['ũ', 'ṳ', 'ŭ'],
        'v': ['ṿ', 'ṽ'],
        'w': ['ẇ', 'ẅ', 'ŵ'],
        'x': ['ẋ', 'ẍ'],
        'y': ['ŷ', 'ÿ', 'ẏ'],
        'z': ['ẓ', 'ž', 'ź']
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
