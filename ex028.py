from random import randint
from time import sleep
nx = randint(0, 5)
s = int(input("Digite um numero de 0 á 5: "))
print("-=-" * 10)
print("Estou pensando......")
print("-=-" * 10)
print("PROCESSANDO...")
sleep(1)
while s not in (0, 5):
    print("Tente novamente! Eu pensei no numero {} e vc no {}".format(nx, s))
    s = int(input("Digite um numero de 0 á 5: "))