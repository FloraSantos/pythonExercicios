lista = []
for c in range(0,2):
    lista.append(int(input('Digite um número:'.format(c))))
print(f'O maior número é {max(lista)}')
print(f'O menor número é {min(lista)}')
