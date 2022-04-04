print('-='*20)
print('Analisador de triângulo')
print('-='*20)
n1 = float(input('Digite o primeiro segmento:'))
n2 = float(input('Digite o segundo segmento:'))
n3 = float(input('Digite o terceiro segmento:'))
if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n2 + n1:
    print('Tem como formar um triângulo!')
else:
    print('Não tem como formar um triângulo!')


