parada = 'N'
opcao = ' '
cont = soma = 0
lista = []
while opcao != parada:
    num = int(input('Digite um número: '))
    opcao = str(input('Quer continuar ? [S/N] ')).upper().strip()
    soma += num
    cont += 1
    lista += [num]
media = soma / cont
print('Você digitou {} números e a média foi {} \nO maior valor foi {} e o menor foi {}'.format(cont, media, max(lista), min(lista)))