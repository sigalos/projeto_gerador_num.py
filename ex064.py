n = int(input('Digite um número [999 para parar]: '))
n = cont = soma = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles é {}'.format(cont, soma))
print('FIM')
