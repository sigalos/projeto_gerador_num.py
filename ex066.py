soma = cont = maior = menor = quant = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    quant += 1
    soma += n
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'No total foram digitados {cont} números e a soma '
      f'entre eles é {soma}, sendo {maior} o número maior e {menor} o menor')
