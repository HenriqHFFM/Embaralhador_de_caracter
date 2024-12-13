import os
import random

# Função de troca de caracteres
def trocar_letras(texto):
    mapeamento = {
        'A': ['Ǟ', 'Ⱥ', 'Ḁ'],
        'B': ['Ḃ', 'Ḅ', 'Ɓ'],
        'C': ['Ƈ', 'Ć', 'Č'],
        'D': ['Ḑ', 'Ḓ', 'Ɖ'],
        'E': ['Ȩ', 'Ḙ', 'Ě'],
        'F': ['Ḟ', 'Ƒ'],
        'G': ['Ġ', 'Ḡ'],
        'H': ['Ȟ', 'Ḥ'],
        'I': ['Ĩ', 'Ḭ', 'İ'],
        'J': ['Ĵ', 'ǰ'],
        'K': ['Ǩ', 'Ḱ', 'Ḳ'],
        'L': ['Ḷ', 'Ḻ'],
        'M': ['Ḿ', 'Ṁ'],
        'N': ['Ṅ', 'Ň', 'Ɲ'],
        'O': ['Ő', 'Ǫ', 'Ṍ'],
        'P': ['Ṕ', 'Ṗ', 'Ƥ'],
        'Q': ['Ꝗ', 'Ꝙ'],
        'R': ['Ȑ', 'Ṙ', 'Ŕ'],
        'S': ['Ș', 'Ṡ'],
        'T': ['Ț', 'Ṫ'],
        'U': ['Ű', 'Ǜ', 'Ṳ'],
        'V': ['Ṽ', 'Ṿ', 'Ʋ'],
        'W': ['Ẃ', 'Ẅ', 'Ŵ'],
        'X': ['Ẍ', 'Ẋ'],
        'Y': ['Ẏ', 'Ŷ', 'Ÿ'],
        'Z': ['Ż', 'Ẑ', 'Ƶ'],

        'a': ['ǡ', 'à'],
        'b': ['ƀ', 'ƃ', 'ḅ'],
        'c': ['ċ', 'č', 'ç'],
        'd': ['ḓ', 'ḑ', 'đ'],
        'e': ['ȩ', 'ě', 'ḙ'],
        'f': ['ƒ', 'ḟ', 'ᵮ'],
        'g': ['ĝ', 'ġ', 'ģ'],
        'h': ['ḩ', 'ḥ', 'ĥ'],
        'i': ['ḭ', 'ĩ', 'į'],
        'j': ['ĵ', 'ʝ', 'ǰ'],
        'k': ['ķ', 'ḱ', 'ǩ'],
        'l': ['ḷ', 'ł', 'ŀ'],
        'm': ['ṁ', 'ṃ', 'ᵯ'],
        'n': ['ṅ', 'ň', 'ñ'],
        'o': ['ọ', 'ő', 'ǫ'],
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
        # Solicitar o caminho completo do arquivo ao usuário
        caminho_original = input("Digite o caminho completo do arquivo .txt que deseja copiar: ")
        caminho_original = os.path.abspath(caminho_original)  # Converter para caminho absoluto

        # Verificar se o arquivo existe
        if not os.path.exists(caminho_original):
            print("Erro: O arquivo especificado não foi encontrado.")
            return

        # Abrir o arquivo original para leitura
        with open(caminho_original, 'r', encoding='utf-8') as arquivo_original:
            conteudo = arquivo_original.read()

        # Substituir letras no conteúdo
        conteudo_modificado = trocar_letras(conteudo)

        # Solicitar o caminho e o nome para o novo arquivo
        caminho_copia = input("Digite o caminho e o nome do novo arquivo .txt (ex: C:\\copia.txt): ")
        caminho_copia = os.path.abspath(caminho_copia)  # Converter para caminho absoluto

        # Criar o novo arquivo e escrever o conteúdo modificado nele
        with open(caminho_copia, 'w', encoding='utf-8') as arquivo_copia:
            arquivo_copia.write(conteudo_modificado)

        print(f"Arquivo copiado e modificado com sucesso para: {caminho_copia}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Executar a função
copiar_arquivo()
