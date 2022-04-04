num = float(input('Digite um número:'))
op = str(input('Deseja continuar (S/N) ?')).upper()
maior = menor = num
count = 1
soma = num
while op != 'N':
     num = float(input('Digite um número:'))
     count += 1
     soma += num
     if num > maior:
         maior = num
     elif num < menor:
            menor = num
     op = str(input('Deseja continuar (S/N) ?')).upper()
print(f'Quantidade de valores digitados {count} e a média dos valores é de {soma/count}')
print(f'O maior número é {maior} e o menor era {menor}')






