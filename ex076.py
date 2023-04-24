listagem = ('Alicate', 35.0,
            'Martelo', 24.75,
            'Furadeira', 295.50,
            'Compasso', 19.55,
            'Trena', 35.5,
            'Espátula', 2,
            'Estilete', 15.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>8.2f}')