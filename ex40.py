print('\033[4;33mMÉDIA DE NOTAS\033[m')

nota1 = float(input('\033[1;36mDigite a primeira nota:\033[m'))
nota2 = float(input('\033[1;36mDigite a segunda nota:\033[m'))
n1 = (nota1 + nota2)/2
if n1 < 5.0:
    print('\033[1;31mVocê foi reprovado\033[m')
elif n1 >= 7.0:
    print('\033[1;37mvocê foi APROVADO!\033[m')
elif n1 >= 5.0 or n1 < 6.9:
    print('\033[1;31mVocê está em recuperação!\033[m')


