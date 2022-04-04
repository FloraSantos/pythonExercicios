f = 0
cont = 0
for c in range(1):
    n1 = int(input('De qual número você deseja ver a tabuada:'))
    while cont < 10:
        cont += 1
        f = n1 * cont
        print(f'{n1} x {cont} = {f}')
print('Fim')