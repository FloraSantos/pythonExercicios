import calendar
ano = int(input('Digite um ano :'))
if calendar.isleap(ano):
    print('É BISSEXTO!')
else:
    print('NÃO É BISSEXTO!')

    