sexo = 'k'
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Qual é o seu sexo [F/M]:')).strip().upper()
    if sexo != 'F' and sexo != 'M':
        print('opção inválida, tente novamente!')
print('Obrigado!')


lista = ['M','F']
sexo = str(input('Digite o seu sexo (M/F) :')).strip().upper()
while sexo not in lista:
    sexo = str(input('Opcao invalida. Digite novamente :')).strip().upper()