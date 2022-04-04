escolha = 'S'
lista =[]
while escolha != 'N':
    lista.append(int(input('Digite um número:')))
    escolha = str(input('Você deseja continuar (S/N) ?')).upper()
print(f'O maior é {max(lista)}')
print(f'O menor é {min(lista)}')