from datetime import date
tempo = 0
tempo1 = 0
for c in range(7):
    data = int(input('Digite sua data de nascimento:'))
    atual = date.today().year
    idade = atual - data
    if idade > 21:
        tempo += 1
        print('Você já atingiu a maioridade!')
        print(f'Você tem {idade} anos')
    else:
        tempo1 += 1
        print('Você ainda não atingiu a maioridade!')
        print(f'Você tem {idade} anos')
print(f'Quantidade de pessoas que já atingiram a maioridade : {tempo}')
print(f'Quantidade de pessoas que ainda não atingiram a maioridade : {tempo1}')