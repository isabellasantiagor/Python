numero=int(input('Digite um número: '))
print(f'Tabuada do {numero}:')
for i in range(1,11,1):
    print(f'{i} X {numero} = {i*numero}')