from time import sleep
n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
cont = 1
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
maior = 0
menor = 0
novo = 0
lista = [n1,n2]
perg = 0
e = 0
print('''
[1] SOMA
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] MAIOR
[5] MENOR
[6] NOVOS NÚMEROS
[7] SAIR 
[8] QUANTIDADE DE VALORES DIGITADOS''')
opc = int(input('Digite sua escolha:'))
if opc == 1:
    print(f'A soma dos valores é igual a {soma}')
elif opc == 2:
    print(f'A suntração dos valores é igual a {sub}')
elif opc == 3:
    print(f'O resultado da multiplicação é {mult}')
elif opc == 4:
    print(f'O maior valor é {max(lista)}')
elif opc == 5:
    if n1 < menor:
        menor = n1
    if n2 < n1:
        menor = n2
    print(f'O menor valor é {min(lista)}')
elif opc == 6:
    c = 0
    c1 = 0
    while c == c1:
        c = int(input('Digite um número:'))
        c1 = int(input('Digite um número:'))
elif opc == 7:
    print('Finalizando programa...')
    sleep(2)
    print('Finalizado!')
elif opc == 8:
    while e != 100:
        e = int(input('Digite um número:'))
        if e != 100:
            cont += 1
        
print(f'A quantidade de números digitados é {cont}')




