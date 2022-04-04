print('-_'*20)
n1 = int(input('Digite um número :'))
print('-_'*20)
print('''\033[7;30;40mConversão de números:\033[m
[\033[1;31m1\033[m] converter para BINÁRIO
[\033[1;31m2\033[m] converter para OCTAL
[\033[1;31m3\033[m] converter para HEXADECIMAL''')
n2 = int(input('Escolha uma opção:'))
if n2 == 1:
    print('você converteu {} para {}'.format(n1,bin(n1)))
elif n2 == 2:
    print('você converteu {} para {}'.format(n1,oct(n1)))
elif n2 == 3:
    print('você converteu {} para {}'.format(n1,hex(n1)))



