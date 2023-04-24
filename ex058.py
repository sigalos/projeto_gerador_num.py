from random import randint
computador = randint(0,10)
print('Olá sou seu computador.. Acabei de pensar um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi ASCHLEY?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Digite um número entre 0 e 10: '))
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('\033[31mDica: jogue um número mais baixo\033[m ')
        else:
            print('\033[32mDica: Jogue um número mais alto.\033[m')
    palpites += 1
print('\033[33mACERTOU ASCHLEY PARABÉNS!!!\033[m')
print('Você tentou \033[7;31m{}\033[m vezes até acertar'.format(palpites))
