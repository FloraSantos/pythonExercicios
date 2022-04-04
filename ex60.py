numero = int(input('Digite o número: '))
cont = numero
fatorial = 1
while cont > 0:
    fatorial *= cont
    cont -=1
print(f'O fatorial de {numero} é {fatorial}')
