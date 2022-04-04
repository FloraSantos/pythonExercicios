from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''(Suas opções)
[0] \033[1;33mPedra\033[m
[1] \033[1;34mPapel\033[m
[2] \033[1;32mTesoura\033[m ''')
jogador = int(input('Faça  sua escolha :'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('=*'*11)
print(f'O computador jogou : {itens[computador]}')
print(f'O jogador jogou : {itens[jogador]}')
print('=*'*11)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('O Jogador é o vencedor!')
    elif jogador == 2:
        print('O computador é o vencedor!')
    else:
        print('Opção invalida')
if computador == 1:
    if jogador == 0:
        print('O computador é o vencedor!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('O jogador é o vencedor!')
    else:
        print('Opção invalida')
if computador == 2:
    if jogador == 0:
        print('O jogador é o vencedor!')
    elif jogador == 1:
        print('O computador é o vencedor!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Opção invalida')






