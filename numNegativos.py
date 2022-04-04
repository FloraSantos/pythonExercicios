cont2 = 0
cont = 0
n1 = 0
c = 'S'
while c != 'N':
    if c != 'S' and 'N':
        print('\033[1;31mResposta inválida!\033[m')
    n1 = float(input('Digite um número:'))
    c = str(input('Deseja continuar (S/N) ?')).upper()
    if n1 < 0:
        cont += 1
    else:
        cont2 += 1
print(f'Quantidade de valores negativos digitados {cont}')