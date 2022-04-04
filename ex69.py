print('COLETANDO DADOS')
mais18 = femmenor20 = men = 0
while True:
    idade = int(input('Digite sua idade :'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo (F/M):')).strip().upper()[0]
        if idade >= 18:
            mais18 += 1
        if sexo == 'F' and idade < 20:
            femmenor20 += 1
        if sexo == 'M':
            men += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Voê quer continuar (S/N) ?')).upper().strip()[0]
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {men} homens cadastrados')
print(f'E temos {femmenor20} mulheres com menos de 20 anos')



