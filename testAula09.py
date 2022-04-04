nome = str(input('Nome completo:')).strip()
print('Seu nome em maisculo é: {}'.format(nome.upper()))
print('Seu nome em minusculo é: {}'.format(nome.lower()))
print('Quantidade de letras ao todo sem os espaços é : {}'.format(len(nome) - nome.count(' ')))
#print('Quantidade de letras que tem no primeiro nome {}'.format(nome.find(' ')))
o = nome.split()
print('Quantidade de letras que tem no primeiro nome {}'.format(len(o[0])))
print('Em split é {}'.format(nome))





