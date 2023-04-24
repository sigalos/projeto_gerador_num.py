print('='*28)
print('{:^28}'.format('10 TERMOS EM PA'))
print('='*28)
primeiro = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao
for l in range(primeiro, decimo + razao, razao):
    print('{}'.format(l), end=' > ')
print('ACABOU')
