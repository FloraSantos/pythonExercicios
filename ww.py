print('================= \033[1;35m CESTA DE COMPRAS \033[1;35m ================= ')
print('Digite x quando tiver colocado todos os produtos!')
lista = ['presunto','pão','ovo','sardinha','alho','cenoura','carne','alface']
print('''MERCADORIAS
- PRESUNTO 4.00
- PÃO 2.00
- OVO 10.00
- SARDINHA 5.00
- ALHO 1.00
- CENOURA 7.00
- CARNE 60.00
- ALFACE 8.00''')
n1 = 0
while n1 != 'x':
        n1 = str(input('Quais produtos da lista você comprou ?')).strip().upper()
print('Ok! Vamos calcular o valor total!')
