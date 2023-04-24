num = list()
num_par = list()
num_impar = list()
while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    if n % 2 == 0:
        num_par.append(n)
    else:
        num_impar.append(n)


    opção = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while opção not in 'SN':
        opção = str(input('Opção inválida! Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opção == 'N':
        break

print(f'Ao total foram digitados {len(num)} valores. São eles {num}')
print(f'Os números pares são {num_par}')
print(f'Os números ímpares são {num_impar}')
