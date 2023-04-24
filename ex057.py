sexo = (str(input('Digite o sexo [M/F]: '))).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Digite novamete: ')).strip().upper()[0]
