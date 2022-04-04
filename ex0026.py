nome = str(input(' Frase :')).strip().upper()
Analisando = input('Analisando...')
print('Quantas vezes aparece a letra (A) ? em {} \n Aparece {} vezes'.format(nome,nome.upper().count('A')))
print('Em que posição o (A) aparece pela primeira vez ?')
print('O (A) aparece pela primeira vez na posição {}'.format(nome.find('A')+1))
print('O A apareceu pela última vez na posição {}'.format(nome.rfind('A')+1))



