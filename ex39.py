from datetime import date
ano = int(input('Em que ano você nasceu ?'))
ano_atual = date.today().year
idade = ano_atual - ano
if idade < 18:
    print(f'Falta {18 - idade} anos para você se alistar no exercito!Em {ano + 18}')
elif idade > 18:
    print(f'Já passou {idade - 18} anos do tempo de se alistar!Era para ter comparecido em {ano + 18}')
elif idade == 18:
    print('Já está na hora de se alistar!')

