x=int(input('Digite o primeiro número:'))
y=int(input('Digite o segundo número:'))
if x>y:
    print(f'A ordem crescente é de {y} e {x}')
elif y>x:
    print(f'A ordem crescente é de {x} e {y}')
else:
    print('Os valores são iguais')