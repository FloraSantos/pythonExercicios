from random import choice
t1 = input('primeira fruta:')
t2 = input('segunda fruta:')
t3 = input('terceira fruta:')
t4 = input('quarta fruta:')
t5 = input('quinta fruta:')
Lista = [t1,t2,t3,t4,t5]
Escolhida = choice(Lista)
print(f' A fruta escolhida para fazer o suco foi de {Escolhida}')



