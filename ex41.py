from datetime import date
ano = int(input('Em que ano você nasceu ?'))
ano_atual = date.today().year
idade = ano_atual - ano
if idade < 9:
    categoria = 'MIRRIM'
elif 9 < idade <= 14:
    categoria = 'INFANTIL'
elif 14 < idade <= 19:
    categoria = 'JUNIOR'
elif 19 < idade <= 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print(f'Você tem {idade} e a sua categoria é {categoria}')


