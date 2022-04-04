import random
from time import sleep
n1 = random.randint(0,5)
nome = str(input('Qual é o seu nome ?'))
print(f'Será que você consegue adivinhar qual é o número ? {nome}')
nn = input('Se sim, é isso que nós vamos ver, vamos lá!')
n2 = input(' Chute um número de 0 á 5:')
print('PROCESSANDO...')
sleep(3)
if n2 == n1:
    print('Parabéns, você acertou!')
else:
    print('Você errou, não foi dessa vez. Tente de novo!')
print(f'A resposta era {n1}')






