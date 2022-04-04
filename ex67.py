from time import sleep

print('=' * 20)
print('TABUADA')
print('=' * 20)
n = 0
while True:
    n = int(input('Digite um número para saber a tabuada (Digite 100 para finalizar!):'))
    if n > 0:
        if n <= 10:
            for c in range(1, 11):
                print(n, 'X', c, '=', n * c)
        elif n > 10 and n <= 99:
            print('\033[31mVocê ultrapassou o limite!\033[m')
            break

    else:
        print('\033[1;31mValor inválido!\033[m')
        print('\033[31mOpa, sem números negativos!\033[m')
        break
    if n == 100:
        print('Finalizando!')
        sleep(2)
        print('Prontinho!')
        break
print('Fim do programa!')


