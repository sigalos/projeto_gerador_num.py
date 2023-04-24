v = float(input("Digite velocidade: "))
if v > 80:
    print("Você foi multado!")
    multa = (v - 80) * 7
    print("\033[4;41mVocê pagará o valor de: R${:.2f}\033[m".format(multa))
print("\033[32mTenha um Bom dia! Diriga com atenção!")