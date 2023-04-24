from datetime import date
atual = date.today().year
sexo = str(input("Qual seu sexo? "))
if sexo in "Feminino feminino Mulher mulher menina":
    print("Você esta dispensada do serviço militar")
elif sexo in "Masculino":
    print("Por favor preencha o formulário:")
nasc = int(input("Digite o ano de seu nascimento: "))
idade = atual - nasc
print("Quem nasceu em {} têm {} anos em {}".format(nasc, idade, atual))
if idade == 18:
    print("Parabéns! Você deve se alistar.")
elif idade < 18:
    saldo = 18 - idade
    print("Ainda faltam {} anos para o alistamento.".format(saldo))
    ano = atual + saldo
    print("Seu ano de alistamento é {}".format(ano))
elif idade > 18:
    saldo = idade - 18
    print("Você deveria ter se alistado a {} anos.".format(saldo))
    ano = atual - saldo
    print("O ano de seu alistamento foi {}.".format(ano))
