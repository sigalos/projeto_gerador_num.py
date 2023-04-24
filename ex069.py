print('-' * 20)
print('CADASTRO DE PESSOAS')
print('-' * 20)
maioridade = mulhermenor = masc = 0
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        maioridade += 1
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        mulhermenor += 1
    while sexo not in 'MF':
        print('Dados incorretos, por favor digite novamente.')
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    p = str(input('Quer continuar cadastrando? [S/N] ')).strip().upper()[0]
    if p == 'N':
        break
    while p not in 'SN':
        print('Dados incorretos, digite novamente por favor.')
        p = str(input('Quer continuar cadastrando? [S/N] ')).strip().upper()[0]
    if p == 'N':
        break
print(f'No total temos {maioridade} pessoas maiores de 18 anos.')
print(f'O total de homens foi {masc}')
print(f'E o total de mulheres com menos de 20 anos é {mulhermenor}.')





