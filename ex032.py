from datetime import date
ano = int(input("Qual ano quer analizar: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é \033[42mBIXESTO\033[m".format(ano))
else:
    print("O ano {} é \033[41mNÃO É BIXESTO\033[m".format(ano))