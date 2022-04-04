print('='*20)
print('\033[1;34mLOJAS GUANABARA\033[m')
print('='*20)

produto = float(input('Qual é o preço do produto ?'))
print('''\033[4;31mFORMAS DE PAGAMENTO\033[m
[1] à vista dinheiro/chegue
[2] à vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão''')
opc = int(input('Escolha uma opção:'))

if opc == 1:
    n1 = produto - (produto * 10 / 100)
    print(f'Você vai pagar um valor de R${n1}')
    print(f'O desconto foi de R${produto - n1}')
elif opc == 2:
    l2 = produto * 5 / 100
    n2 = produto - (produto * 5 / 100)
    print(f'Você vai pagar um valor de R${n2}')
    print(f'O desconto foi de R${l2}')
elif opc == 3:
    print('Não tem desconto')
elif opc == 4:
    n3 = int(input('Vai parcelar quantas vezes no cartão ?'))
    n4 = produto + (produto * 0.20)
    print(f'Você vai pagar {n4} em {n3}x de R${n4/n3}')






