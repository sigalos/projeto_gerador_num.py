from time import sleep
num = int(input("Digite um número: "))
result = num % 2
print("-=-" * 13)
print("Estou pensando...")
print("-=-" * 13)
sleep(2)
if result == 0:
    print("\033[1;42m{} é um numero Par\033[m".format(result))
else:
    print("\033[1;31m{} é um número Impar\033[m".format(result))
