lanche = 'suco', 'paçoca', 'bombom', 'sorvete', 'espetinho'
#for comida in lanche:
 #   print(f'Hoje comi {comida}')

#for cont in range(0, len(lanche)):
 #   print(f'Hoje eu comi {lanche[cont]}')

for pos, comida in enumerate(lanche):
    print(f'Hoje eu vou comer {sorted(lanche)} posicão {pos}')
print('Estou satisfeito')