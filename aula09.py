nome = str(input("Digite seu nome completo: ")).strip()
print("Analizando seu nome:")
print("Seu nome em letras maiúsculas: {}".format(nome.lower()))
print("Seu nome em letras minúscula: {}".format(nome.upper()))
print("Seu primeiro nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
#print ("Seu primeiro nome tem {} letras.".format(nome.find(" ")))
separa = nome.split()
print("Seu segundo nome é {}\nEle tem {} letras".format(separa[1].upper(), len(separa[1])))#40042040

