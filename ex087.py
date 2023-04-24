matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor na posição {linha} {coluna}: '))
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]
    print()
print('-=' * 30)
print(f'A soma dos números pares {spar}')
for linha in range(0, 3):
    scol += matriz[linha][2]
print(f'Os valores da 3ª coluna são: {scol}')
for coluna in range(0, 3):
    mai = matriz[coluna][1]

print(f'O maior valor da segunda linha é {mai}')
