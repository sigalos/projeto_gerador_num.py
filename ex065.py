resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm

    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} e a média foi {:.2}'.format(quant, média))


print('Maior valor digitado foi {} e o menor valor digitado foi {}'.format(maior, menor))
