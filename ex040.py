n1 = float(input("Digite valor da nota 1: "))
n2 = float(input("Didite valor da nota 2: "))
média = (n1 + n2) / 2
if média < 5.0:
    print("Sua média foi {}, estude mais REPROVADO".format(média))
elif média >= 5.0 and média < 7:
    print("RECUPERAÇÃO sua media foi {}".format(média))
elif média > 7.0:
    print("Aluno APROVADO sua média foi {}.".format(média))
