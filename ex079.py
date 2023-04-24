números = list()
números.sort()
while True:
    n = int(input('Digite um valor:'))
    if n not in números:
        números.append(n)
        print(f'Valor {n} foi adicionado com sucesso!!!')
    else:
        print(f'O valor {n} já existe na lista e não pode ser adicionado. ')
    opção = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opção == 'N':
        break
print(números)
