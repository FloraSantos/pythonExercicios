l1 = int(input('Primeira reta: '))
l2 = int(input('Segundo reta: '))
l3 = int(input('Terceira reta: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Essas retas podem formar um triangulo!')
    if l1 == l2 == l3:
        print('O triângulo é do tipo equilátero.')
    elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
        print('O triângulo é do tipo isósceles.')
    elif l1 != l2 != l3 != l1:
        print('O triângulo é do tipo escaleno.')
else:
    print('Essas retas não podem formar um triangulo!')

