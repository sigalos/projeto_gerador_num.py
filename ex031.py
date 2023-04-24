from datetime import date
ano = int(input("Qual ano quer analizar: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é bixesto".format(ano))
else:
    print("O ano {} não é bixesto".format(ano))