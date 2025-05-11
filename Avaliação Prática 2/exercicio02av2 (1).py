a=float(input('Digite o primeiro valor:'))
b=float(input('Digite o segundo valor:'))
c=float(input('Digite o terceiro valor:'))
maior= max(a,b,c)
if a==b==c:
    print('Os números são iguais.')
else:
    print(f'O maior número entre {a},{b} e {c} será {maior}.')
