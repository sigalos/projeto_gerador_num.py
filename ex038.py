n1 = int(input("Digite primeiro número:"))
n2 = int(input("Digite o segundo número"))
if n1 > n2:
    print("Comparando os numeros digitados verificamos que o \033[33m{}\033[m é maior que \033[33m{}\033[m".format(n1, n2))
elif n2 > n1:
    print("Comparando os dois numeros descobrimos que \033[33m{}\033[m é maior que \033[33m{}\033[m".format(n2, n1))
else:
    print("\033[34mNão existe valor maior! Os dois são iguais.\033[m")
