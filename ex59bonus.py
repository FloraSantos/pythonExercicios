from time import sleep

n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
soma = n1 + n2
maior = 0
mult = n1 * n2
lista = [1, 2, 3, 4, 5]
cont = 0
print('=' * 20)
print('''MENU
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
print('=' * 20)
opc = int(input('Digite sua opção:'))
if opc == 1:
    print(f'A soma dos valores {n1} + {n2} é = {soma} ')
elif opc == 2:
    print(F'A multiplicação de {n1} x {n2} é = {mult}')
elif opc == 3:
    if n1 > n2:
        maior = n1
    elif n2 > n1:
        maior = n2
    print(f'O maior valor é {maior}')
elif opc == 4:
    c = 0
    c1 = 0
    while c == c1:
        c = int(input('Digite um número:'))
        c1 = int(input('Digite um número:'))
elif opc == 5:
    print('Finalizando...')
    sleep(2)
    print('Fim do programa!')
elif opc != lista:
    print('\033[1;31mResposta inválida!\033[m')



