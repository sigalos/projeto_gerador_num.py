numeros = [[], []]
valor = 0
for c in range(1, 7):
    valor = int(input(f'Digite  o {c}º número: '))
    if c % 2 == 0:
       numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()
print(f'Lista de números pares: {numeros[0]}')
print(f'Lista de números ímpares: {numeros[1]}')




