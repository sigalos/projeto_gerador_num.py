tot = mais = cont = menor = 0
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    tot += preco
    if cont == 1:
        menor = preco
        produto = nome
    else:
        if preco < menor:
            menor = preco
            produto = nome
    if preco > 1000:
        mais += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continua not in 'SN':
            print('\033[31mOpção inválida!\033[mTente novamente.')
    if continua == 'N':
        break

print(f'O valor total das compras foi R$ {tot:.2f}')
print(f'No total temos {mais} produtos com valor acima de R$ 1000.00')
print(f'O produto {produto} que custa R$ {menor:.2f} têm o menor valor')
