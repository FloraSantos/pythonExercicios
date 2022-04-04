print ('=-'*20)
print ('LOJA SUPER BARATÃO')
print ('=-'*20)
menor = 0
tot = 0
exp = 0
c = 1
mb = ' '
while True:
    nome = str(input('Nome do produto: '))
    preço = int(input('Preço do produto: R$'))
    tot += preço
    if preço >= 1000:
        exp += 1
    if c == 1:
        menor = preço
        mb = nome
    else:
        if menor > preço:
            menor = preço
            mb = nome
    c += 1
    while True:
        af = str (input('Quer adicionar mais compras ao carrinho? [S/N]'))
        if af in 'SsNn':
            break
    if af in 'Nn':
        break
print ('=-'*20)
print (f'''O total gasto foi de R${tot}.
{exp} produto(s) custam mais de R$1000.
O produto mais barato é o(a) {mb} e custa R${menor}.''')



Genese Barbosa
Genese Barbosa
há 8 meses