valor = int(input('Qual é o valor do seu sálario ?'))
print('Você vai receber um aumento, vamos calcular')
n = valor+(valor*(10/100))
m = valor+(valor*(15/100))
if valor >= 1250:
    print('você ganhou um aumento de 10%, então seu sálario vai ser reajustado para {:.2f}'.format(n))
else :
    print('Você vai receber um reajuste no sálario de 15%, resultando em um valor de {:.2f}'.format(m))
