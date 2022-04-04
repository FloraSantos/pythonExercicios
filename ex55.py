n1 = float(input('Digite o seu peso:'))
maior = n1
menor = n1
for c in range(1,4+1):
    n1 = float(input('Digite seu peso:'))
    if n1 >= maior:
        maior = n1
    elif n1 <= menor:
        menor = n1
print(f'O maior peso é de {maior} e o menor é de {menor}')
