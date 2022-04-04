distancia = float(input('É uma viagem de quantos km ?'))
n = distancia * 0.50
m = distancia * 0.45
if distancia <= 200:
    print('O valor da passagem vai ser de {}'.format(n))
else:
   print('O valor da passagem vai ser de {}'.format(m))

