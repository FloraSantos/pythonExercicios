velocidade = int(input('Seu carro está a quantos km/h ?'))
if velocidade >= 80:
    v = velocidade - 80
    i = v * 7
    print('Você foi multado!')
    print(f'O valor da multa é de {i}')
else:
    print('Sua velocidade está ótima')
