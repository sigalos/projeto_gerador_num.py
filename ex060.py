from time import sleep
n = int(input('Digite um número: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end=' ')
    sleep(1)
    print('x ' if c > 1 else '= {}'.format(f), end='')
    f *= c
    c -= 1
    sleep(1)


