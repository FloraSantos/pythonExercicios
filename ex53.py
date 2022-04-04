for c in range(0,1):
    frase = str(input('Digite uma frase :')).strip().replace(' ','').upper()
    n1 = frase[::-1]
    if n1 == frase:
        print('A frase é um palídromo')
    else:
        print('Não é um palídromo')
    print(n1)

