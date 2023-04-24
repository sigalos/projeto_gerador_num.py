frase = str(input('Digite a frase: ')).strip().upper()
palaras = frase.split()
junto = ''.join(palaras)
'''DESSA FORMA UTILIZANDO FATIAMENTO'''
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um \033[33mPALINDROMO')
else:
    print('\033[32mEsta frase não forma um palindromo.')