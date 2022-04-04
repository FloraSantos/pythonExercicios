import random
num = random.randint(1,3)
print('Eu tenho um presente para você! Mas você só vai receber hoje se escolher a opção do dia.')
print('''Tente a sorte com uma das opções abaixo:\033[1;33m
[1] presente
[2] presente 
[3] presente\033[m''')
n1 = int(input('Escolha um número:'))
if n1 == num:
    print(f'o resultado foi : {num}')
    print('Parabéns! Você vai receber o seu presente hoje')
elif n1 > 3:
    print('\033[1;31mOpção inválida!\033[m')
else:
    print(f'o resultado foi : {num}')
    print('Que pena, você vai ter que esperar mais um pouquinho...')
