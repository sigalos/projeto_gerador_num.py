times = ("Flamengo", "Santos",  "Palmeiras", "Grêmio",
             "Atletico Paranaense", "São Paulo", "Internacional",
             "Conrithians", "Fortaleza", "Goias", "Bahia", "Vasco",
             "Atletico Mineiro", "Fluminense", "Botafogo", "Ceará",
             "Cruzeiro", "CSA", "Chapecoense", "Avaí")
print('-' * 20)
print(f'Os quatro primeiros times são: {times[0:4]}')
print('-' * 20)
print(f'Os quatro últimos times são: {times[16:]}')
print('-' * 20)
print(f'Lista de times em ordem alfabética: {sorted(times)}')
print('-' * 20)
res = ' '
while res not in 'SN':
    res = str(input('Deseja saber em qual posição seu time esta? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
    else:
        opção = str(input('Qual é seu time? '))
        print(f'O time do(a) \033[32m{opção}\033[m está na {times.index(opção) + 1}ª posição.')
print('-=' * 10)
print('FIM DO PROGRAMA')
print('-=' * 10)




