#---------------------------------------#
# Desenvolvedor: Fabio Eduardo do Vale  #
# Data: 13/06/2019                      #
# Versão: 0.0.1                         #
#---------------------------------------#
import os
import json
import urllib.request
import random

from unicodedata import normalize

def obterCidades(url: str, uf: str = 'PR') -> list:

    os.system('cls')
    _url = url
    _uf = uf
    contador = 0
    cidades = []

    try:
        resposta = urllib.request.urlopen(_url).read()
        resultado = json.loads(resposta)
        
        estados = resultado['estados']
        for estado in estados:
            if(estado['sigla'] == _uf.upper()):
                
                for cidade in estado['cidades']:
                    cidades.append(cidade)
    
        return cidades

    except Exception as erro:
        print("Ocorreu um erro ao carregar o arquivo.")
        print("Erro: {}".format(erro))


def sortearCidade(cidades: list) -> str:
    
    sorteio = random.randrange(len(cidades))
    
    cidade = cidades[sorteio]
    cidade = normalize('NFKD', cidade).encode('ASCII', 'ignore').decode('ASCII')

    return (cidade.lower())
    


def jogar():

    cidades = obterCidades(link)
    palavra_secreta = sortearCidade(cidades)

    letras_erradas      = []
    letras_corretas     = []
    continuar           = True

    contador = 0

    while True:
        
        os.system('cls')

        palavra_temporaria = ''
        for x in range(0, len(palavra_secreta)):
            if palavra_secreta[x] in letras_corretas:
                palavra_temporaria  = palavra_temporaria + ' ' + palavra_secreta[x].upper()
            else:
                palavra_temporaria = palavra_temporaria + ' ' + ' _ '

        print("")
        print(palavra_temporaria)
        print("")

        print("")
        print("Letras erradas: ")
        print(letras_erradas)
        print("")

        print("Letras corretas: ")
        print(letras_corretas)
        print("")
        
        palavra_revelada = True
        for x in range(len(palavra_secreta)):
            if letras_corretas.count(palavra_secreta[x]) <= 0:
                palavra_revelada = False

        if not palavra_revelada:

            if len(letras_erradas) < 5:
                
                letra = input("Tenta a sorte, chuta uma letra: ")

                if letra in palavra_secreta:
                    if letra not in letras_corretas:
                        letras_corretas.append(str(letra))
                else:
                    if letra not in letras_erradas:
                        letras_erradas.append(str(letra))
            else:
                print("Perdeu playBoy...")
                print("A palavra secreta era: " + palavra_secreta)
                break
        else:
            print("Opa, acho que você acertou...")
            print("A palavra secreta é: " + palavra_secreta)
            break

if __name__ == "__main__":
    
    link = 'https://gist.githubusercontent.com/letanure/3012978/raw/36fc21d9e2fc45c078e0e0e07cce3c81965db8f9/estados-cidades.json'
    jogar()            