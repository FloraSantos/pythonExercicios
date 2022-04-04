num = float(input('Digite um número: '))
op = str(input('Deseja contiuar? [S/N]: ')).upper()
maior = menor = num
cont = 1
soma = num
while op != 'N':
    num = float(input('Digite um número: '))
    cont += 1
    soma += num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    op = str(input('Deseja contiuar? [S/N]: ')).upper()
print('Você digitou {} números e a média entre eles foi de {}' .format(cont, soma/cont))
print('O maior valor foi {}  e o menor foi {}' .format(maior, menor))