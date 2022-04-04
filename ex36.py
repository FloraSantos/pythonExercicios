from time import sleep
print('Empréstimo bancário')
casa = float(input('Qual é o valor da casa ?'))
salario = float(input('De quanto é o seu salário ?'))
anos = int(input('Em quantos anos você pretende pagar ?'))
n1 = salario * 0.30
parcela = casa / (anos * 12)
print('Processando...')
sleep(3)
if parcela >= n1:
    print('O empréstimo foi negado!')
else:
    print('O empréstimo foi aprovado!')
print('Para pegar uma casa de {} em {} anos, você vai ter que pagar parcelas de R${:.2f}'.format(casa,anos,parcela))

