from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 4):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade < 18:
        totmenor += 1
    else:
        totmaior += 1
print('O total de pessoas maiores é {}'.format(totmaior))
print('O total de pessoas menores é {}'.format(totmenor))
