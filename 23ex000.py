n2 = int(input('informe o número:'))
print(f'Analisando o número : {n2}')
u = n2//1 % 10
d = n2//10 % 10
c = n2//100 % 10
m = n2//1000 % 10

print(f'Unidade: {u} \n Dezena:{d} \n Centena:{c}\n Milhar:{m}')

