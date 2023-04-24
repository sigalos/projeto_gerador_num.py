a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print("O menor valor digitado é \033[32m{}\033[m".format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O maior valor digitado é \033[32m{}\033[m".format(maior))
