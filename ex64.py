count = 0
soma = 0
num = 1
print('Digite 999 quando desejar encerrar o programa!')
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        count += 1
        soma += num
print(f'Quantos números foram digitados ? {count}')
print(f'A soma dos números digitados é {soma}')
