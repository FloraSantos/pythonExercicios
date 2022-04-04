soma1 = 0
soma = 0
for c in range(1,501):
    if c % 3 == 0:
        if c % 2 != 0:
            soma += 1
            soma1 += c
print(f'A quantidade de vezes que se encontrou os multiplos de 3: {soma}\n a soma final é de {soma1}')
