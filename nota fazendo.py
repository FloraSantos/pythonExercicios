cont = 0
for c in range(10):
    nota = float(input('Digite sua nota :'))
    if nota >= 7:
        cont += 1
        if nota >= 7.0:
            print('Parabéns, você obteve a média necessária!')
    else:
        print('Você não conseguiu atingir a pontuação!')
print(f'Quantidade de pessoas que alcançaram a nota:{cont}')
