while True:
    n = int(input('Qual número que deseja ver a tabuada: '))
    if n < 0:
        break
    print('-' * 20)
    for c in range(1, 11):
        print(f'{n} x {n} = {n * c}')
    print('-' * 20)
