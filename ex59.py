from time import sleep
n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
sm = n1 + n2
mu = n1 * n2
maior = 0
lista = [1,2,3,4,5]
print(''' MENU
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
opc = int(input('Digite sua opção:'))
if opc == 1:
    print('O valor da soma entre {} + {} é {} '.format(n1,n2,sm))
elif opc == 2:
    print(f'O resultado da multiplicação entre {n1} x {n2} é {mu}')
elif opc == 3:
    if n1 > n2:
        maior = n1
        print('Esse é o maior {maior}')
    elif n2 > n1:
        maior = n2
        print(f'Esse é o maior {maior}')
elif opc == 4:
    c = 1
    c2 = 1
    while c == c2:
        c = int(input('Digite um número:'))
        c2 = int(input('Digite um número:'))
elif opc == 5:
    sleep(2)
    print('Finalizando...')
    sleep(1)
    print('Fim do programa!')
elif opc != lista:
    print('\033[1;31mOpção inválida! Tente novamente\033[m')



