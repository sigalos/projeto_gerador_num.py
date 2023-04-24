aluno = dict()
aluno['NOME'] = str(input('Nome: '))
aluno['MÉDIA'] = float(input('Média: '))
conf = ''
if aluno['MÉDIA'] >= 5:
    conf = 'APROVADO'
else:
    conf = 'REPROVADO'
aluno['SITUAÇÃO'] = conf
print('-=' * 20)
for k, v in aluno.items():
    print(f'{k:<13} {"=":^13} {v:<13}')
print(f'{" FINAL DO PROGRAMA ":=^40}')
