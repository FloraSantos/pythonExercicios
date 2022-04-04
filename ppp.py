from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('O QUE DESEJA FAZER COM OS NÚMEROS DIGITADOS?')
    opcao = int(input('''
        [ 1 ] - Somar os números
        [ 2 ] - Multiplicar os números
        [ 3 ] - Mostrar maior valor
        [ 4 ] - Digitar novos números
        [ 5 ] - Sair do programa 
        Selecione uma opção: '''))
    if opcao == 1:
        print('A SOMA entre {} e {} é igual a {}.'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A MULTIPLICAÇÃO ENTRE {} e {} é igual a {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('O MAIOR número digitado foi {}.'.format(n1))
        else:
            print('O MAIOR número digitado foi {}.'.format(n2))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    sleep(1)
    print('=-='*20)
print('FIM!!!')
