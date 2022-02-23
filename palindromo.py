def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    return palabra==palabra_invertida;


def run():
    palabra = input('escribe una palabra: ')
    es_palidromo = palindromo(palabra)
    if es_palidromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__=='__main__':
    run()