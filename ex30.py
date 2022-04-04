from time import sleep
n1 = int(input('Digite um número :'))
print('PROCESSANDO...')
sleep(3)
n2 = n1 % 2
if n2 == 0:
    print('Ele é par!')
else:
    print('Ele é ímpar!')
