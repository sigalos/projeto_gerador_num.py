palavras = ('foca', 'brhama', 'bola', 'gato',
         'ventilador', 'chave', 'cachorro',
         'porta', 'planta', 'televisor')
for p in palavras:
    print(f'\nNa palavra {p.upper():.^15} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
