from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10),
     randint(0, 10), randint(0, 10))
print('lista de números sorteados foram: ', end='')
for c in n:
    print(f'{c} ')
print(f'\nO maior número da lista é :{max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
