import random
print('\033[1;34mTENTE ADIVINHAR!!\033[m')
computador = random.randint(0,10)
count = 0
c = 1
while c != computador:
    c = int(input('Chute um número:'))
    count += 1
    if c != computador:
        print('Tente novamente!')
print('\033[1;35mVOCÊ ACERTOU!!\033[m')
print(f'Foram necessários {count} tentativas para acertar!')
