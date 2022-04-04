c = int(input('Digite um velor:'))
n1 = str(input('Você quer continuar ?')).upper()
soma = c
count = 1
media = 0
lista = [c]
while n1 == 'S':
    c = int(input('Digite um velor:'))
    count += 1
    soma += c
    media = soma / count
    lista += [c]
    n1 = str(input('Você quer continuar ?')).upper()
    if n1 != 'S':
        print('Valores coletados!')


print(f'Quantidade de pessoas que participaram da pesquisa: {count}')
print(f'Média dos valores digitados {media}')
print('O maior número é {} e o menor numero é {}'.format(max(lista),min(lista)))
