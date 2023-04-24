from random import randint
from time import sleep
print('\033[34;44m=\033[m' * 34)
print(f'\033[1;39;44m{"GERADOR DE JOGOS DA MEGA SENA":^34}\033[m')
print('\033[34;44m=\033[m' * 34)
lista = list()
jogos = list()
quant = int(input('\033[40m Quantos jogos deseja sortear? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'\033[40m{f" {i+1}º JOGO: {l}":<34}\033[m')
    sleep(1)
print(f'\033[44m{"FINAL DO PROGRAMA":^34}\033[m')
print(f'\033[44m{"* BOA SORTE *":^34}\033[m')

