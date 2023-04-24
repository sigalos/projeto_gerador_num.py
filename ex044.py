print("{:=^40}".format(" LOJAS MOACIR "))
preço = float(input("Preço das compras: R$"))
print('''Forma de pagamento
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input("Qual é a opção: "))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = preço / 2
    print("Sua compra será parcelada em 2x iguais de R${:.2f}".format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input("Quantas parcelas? "))
    parcela = total / totparc
    print("Sua compra será parcelada em {}x iguais de R${:.2f}".format(totparc, parcela))
else:
    total = preço
    print("OPÇÃO INVÁLIDA! Tente novamente.")
print("Sua compra de R${:.2f} custará R${:.2f}".format(preço, total))

