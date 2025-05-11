a=float(input('Digite o valor da reta A:'))
b=float(input('Digite o valor da reta B:'))
c=float(input('Digite o valor da reta C:'))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('As retas formam um triângulo equilátero.')
    elif a == b or a == c or b == c:
        print('As retas formam um triângulo isósceles.')
    else:
        print('As retas formam um triângulo escaleno.')
else:
    print('Não é um triângulo.')
