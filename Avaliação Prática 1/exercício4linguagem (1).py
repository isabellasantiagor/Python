x=int(input('Digite um número: '))
y=int(input('Digite outro número: '))
if x>y:
    print(f'A ordem crescente é de: {y} e {x}')
elif y>x:
    print(f'A ordem crescente é de: {x} e {y}')
else:
    print('Os valores são iguais.')