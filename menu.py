from time import sleep
n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
rf = n1 + n2
sm = n1 * n2
maior = 0
lista = [1,2,3,4,5]
print('''
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
opc = int(input('Digite sua opção:'))
if opc == 1:
    print(f'A soma de {n1} e {n2} é igual a {rf}')
elif opc == 2:
    print(f'A multiplicação de {n1} e {n2} é igual a {sm}')
elif opc == 3:
    if n1 > n2:
        maior = n1
        print(f'O maior valor apresentado é {maior}')
    elif n2 > n1:
        maior = n2
    print(f'O maior valor apresentado é {maior}')
elif opc == 4:
    c = 0
    c2 = 0
    while c == c2:
         c = int(input('Digite um número:'))
         c2 = int(input('Digite um número:'))
elif opc == 5:
    print('Finalizando o programa...')
    sleep(2)
    print('Encerramento concluido!')
elif opc != lista:
    print('\033[1;31mOpção inválida!\033[m')
