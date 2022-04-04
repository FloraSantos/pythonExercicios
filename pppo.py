print('Quando a quantidade de pessoas selecionadas para a pesquisa terminar, digite 0\n')

print('\033[1;33m=$\033[m'* 20)
count = 0
n1 = float(input('Você saiu com quanto de dinheiro ?'))
while n1 != 0:
    n1 = float(input('Você saiu com quanto de dinheiro ?'))
    count +=1
print(f'Quantidade de pessoas que participaram da pesquisa: {count}')

print('\033[1;33m=$\033[m'* 20)