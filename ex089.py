ficha = []
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite 1º nota: '))
    nota2 = float(input('Digite 2º nota: '))
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('\033[31mOpção inválida!\033[mDeseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 20)
print(f'{"Nº":^8}{"NOME":^20}{"MÉDIA":^12}')
print('-' * 40)
for i, d in enumerate(ficha):
    print(f'{i:^6}{d[0]:^24}{d[2]:^10}')

print('-' * 40)
while True:
    opção = int(input('Deseja ver a nota de qual aluno:'))
    if opção == 99:
        break
    if opção <= len(ficha) - 1:
        print(f'O aluno {ficha[opção][0]} suas notas são {ficha[opção][1]}')
