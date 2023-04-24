from time import sleep
n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
opção = 0
while opção != 5:
    print('''    \033[33m[ 1 ] Soma
    [ 2 ] Multipicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa\033[m''')
    opção = int(input('Qual é sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma de {} + {} = {}'.format(n1, n2, soma))
    elif opção == 2:
        multi = n1 * n2
        print('A multiplicação de {} x {} = {}'.format(n1, n2, multi))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        n1 = int(input('primeiro valor: '))
        n2 = int(input('segundo valor: '))
    else:
        print('\033[31mVocê digitou um número inválido!\033[m\n\033[32mPor favor tente novamente.\033[m')
    print('-=' * 12)
    sleep(1)
print('\033[32mFim do programa. Volte sempre.\033[m')
