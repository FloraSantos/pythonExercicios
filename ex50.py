soma = 0
for c in range(1,7):
    n1 = int(input('\033[1;34mDigite um número:\033[m'))
    if n1 % 2 == 0:
        soma += n1
    elif n1 % 2 != 0:
        print('\033[1;31mValor descartado!\033[m')
print(f'Resultado da soma: {soma}')
print('FIM DO PROGRAMA!')

