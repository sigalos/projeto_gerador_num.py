pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(int(input('Digite o peso da pessoa: ')))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    res = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('\033[31mOpção inválida!\033[m Deseja continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break

print('-=' * 20)
print(f'Ao total {len(pessoas)} pessoas foram cadastradas')
print('Lista de pessoas com maior peso: ', end='')
for peso in pessoas:
    if peso[1] == maior:
        print(f'[{peso[0]}] ', end='')
print()
print(f'Lista de pessoas com menor peso: ', end='')
for peso in pessoas:
    if peso[1] == menor:
        print(f'[{peso[0]}] ', end='')
print()
