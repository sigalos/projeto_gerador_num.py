expre = str(input('Digite sua expressão: '))
pilha = list()
for simbolo in expre:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print(expre)
print(pilha)
