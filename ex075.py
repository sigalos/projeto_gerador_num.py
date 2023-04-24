núm = (int(input('Digite um número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os números {núm}')
print(f'O número 9 apareceu {núm.count(9)} vezes.')
if 3 in núm:
    print(f'O número 3 foi digitado a primeira vez na posição {núm.index(3)+1}')
print(f'Os números pares digitados são ', end='')
for n in núm:
    if n % 2 != 0:
        print(n, end=' ')




