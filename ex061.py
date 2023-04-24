print('='*28)
print('{:^28}'.format('10 TERMOS EM PA'))
print('='*28)
primeiro = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' > ')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM no total foram {} termos'.format(total))

