soma = count = menor = 0
c = 1
mp = ' '
while True:
    nome = str(input('Nome do produto:')).strip()
    preco = float(input('Digite o preço do produto :'))
    soma += preco
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Você quer continuar (S/N) ?')).upper().strip()[0]
    if preco > 1000:
        count += 1
    if c == 1:
        menor = preco
        mp = nome
    else:
        if menor > preco:
            menor = preco
            mb = nome
    c += 1
    if cont == 'N':
        break

print(f'A soma total dos produtos é de {soma}')
print(f'Quantidade de preços maiores que R$ 1000 é de {count}')
print(f'O nome do produto mais barato é {mp} e o preço é {menor}')




