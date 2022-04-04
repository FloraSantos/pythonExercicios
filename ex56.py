media = 0
fem = 0
maior = 0
nomef = 0
for c in range(1,5):
    print(f'----{c}ª PESSOA----')
    nome = input('Qual é o seu nome ?').strip()
    idade = int(input('Qual é a sua idade ?'))
    sexo = input('Qual é o seu sexo (M/F):').upper()
    media += idade/4
    if sexo == 'M' and idade > maior:
        maior = idade
        nomef = nome
    if sexo == 'F' and idade < 20:
        fem += 1
print(f'A média de idade do grupo é de {media}')
print(f'O nome do homem mais velho é {nomef} ele tem {maior}')
print(f'A quantidade de mulheres com menos de 20 anos é de {fem}')



