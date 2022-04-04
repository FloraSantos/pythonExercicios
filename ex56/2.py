media = 0
maior = 0
fem = 0
n = 0
for p in range(1, 5):

    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper()
    media += idade / 4
    if idade > maior and sexo == "M":
        maior = idade
        n = nome
    if sexo == "F" and idade < 20:
        fem += 1
print(f"A média de idade do grupo é de {media} anos")
print(f'O Homem mais velho tem {maior} e se chama {n}')
print(f"Ao  todo são {fem} mulheres com menos de 20 anos")