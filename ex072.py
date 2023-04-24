cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    usuario = int(input('Digite um número de 0 á 20: '))
    if usuario < 0 or usuario > 20:
        print('Digite novamente. ', end='')
    elif 0 <= usuario <= 20:
        print(f'O número que você digitou foi {cont[usuario]}')
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Deseja continuar. [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
print('=' * 15)
print('FIM DO PROGRAMA')
print('=' * 15)
