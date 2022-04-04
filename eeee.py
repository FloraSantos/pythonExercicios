n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
lista = [1,2,3,4,5]
opc = 0
while opc != 5:
    print('''
    [1] SOMAR
    [2] MULT
    [3] SUB
    [4] NÚMEROS NOVOS
    [5] SAIR''')
    opc = int(input('Digite sua opção:'))
    if opc == 1:
        soma = n1 + n2
        print(f'A soma dos valores é {soma}')
    elif opc == 2:
        mult = n1 * n2
        print(f'A multiplicação dos valores é {mult}')
    elif opc == 3:
        sub = n1 + n2
        print(f'O resultado da subtração é {sub}')
    elif opc == 4:
        c = 0
        c1 = 0
        while c == c1:
            c = int(input('Digite um número:'))
            c1 = int(input('Digite um número:'))
    elif opc == 5 :
        print('\033[1;35mFim do programa!\033[m')
    elif opc != lista:
        print('\033[1;31mValor inválido!\033[m')
        