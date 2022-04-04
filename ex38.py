n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um valor:'))
if n1 > n2:
    print(f'{n1} é o maior emtre {n1} e {n2}')
elif n2 > n1:
    print(f'{n2} é o maior entre {n1} e {n2}')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais')
