soma = 0
soma1 = 0
for c in range(1,7):
    perg = int(input('Digite um número:'))
    soma += perg
    soma1 += 1
    if perg % 2 == 0:
        print('Valor válido!')
print(f'A soma dos números pares é igual a {soma}\n Quantidade : {soma1}')

