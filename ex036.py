casa = float(input("Qual valor da casa: R$"))
salário = float(input("Qual o seu salário: R$"))
anos =int(input("Quantos anos de financiamento: "))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print("Para pagar uma casa no valor de R${:.2f} em {} anos,".format(casa, anos), end="")
print(" a prestação será de R${:.2f}".format(prestação))
if prestação <= mínimo:
    print("Financiamento aprovado!")
else:
    print("Financiamento não aprovado!")

