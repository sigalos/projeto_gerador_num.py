r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar um triangulo ", end="")
    if r1 == r2 == r3:
        print("EQUILÁTERO")
    elif r1 != r2 != r3 != r1:
        print("ESCÁLENO")
    else:
        print("ISÓCELES")
else:
        print("Os elementos acima não podem formar triângulo!")
