from time import sleep
print('\033[33m{:#^23}\033[m'.format(' CONTAGEM REGRESSIVA '))
for c in range(10, -1, -1):
    sleep(0.5)
    print('\033[32m{}\033[m'.format(c), end=' ')
print('\033[7;33m{}\033[m'.format('FIM'))
