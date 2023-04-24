soma = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
print('O somatório de todos os numeros é igual a {}'.format(soma))
