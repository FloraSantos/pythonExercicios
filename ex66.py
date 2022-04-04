n = soma = count = 0
while True:
    n = int(input('Digite um valor:'))
    if n == 999:
        break
    soma = soma + n
    count = count + 1

print(f'A soma dos valores é de {soma}')
print(f'Quantidade de valores digitados {count}')

