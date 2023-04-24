print("-=-" * 20)
print("Analizador de triangulos")
print("-=-" * 20)
r1 = float(input("Digite valor 1: "))
r2 = float(input("Digite valor 2: "))
r3 = float(input("Digite valor 3: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar um triangulo!")
else:
    print("Os segmentos acima não podem formar triangulo!")
