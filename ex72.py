sequence = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
            'sete', 'oito',
            'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n1 = int(input('Digite um número entre (0 e 20):'))
    if n1 < 0:
        print('\033[31mTente novamente! Não aceito números menores que zero!\033[m')
    elif n1 > 20:
        print('\033[31mTente novamente! Não aceito números maiores que vinte!\033[m')
    else:
        print(f'O número {n1} por extenso é {sequence[n1]}')
    conti = ' '
    while conti not in 'SsNn':
        conti = str(input('Quer continuar (S/N) ?')).strip().upper()[0]
    if conti == 'N':
        break
print('Fim do programa!')


