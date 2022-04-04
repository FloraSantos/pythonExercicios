num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0
while cont < 10:
    print(num, end='-> ')
    num += razao
    cont += 1
print('Acabou')