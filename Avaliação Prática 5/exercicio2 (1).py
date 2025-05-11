inicial=int(input('Valor incial: '))
final=int(input('Valor final: '))
print('Fahrenheit | Celsius')
if inicial<final or inicial==final:
    for fahrenheit in range(inicial,final+1,1):
        celsius=(5*(fahrenheit - 32))/9
        print(f'{fahrenheit}ºF | {celsius:.3f}ºC')
else:
    for fahrenheit in range(inicial,final-1,-1):
        celsius=(5*(fahrenheit - 32))/9
        print(f'{fahrenheit}ºF | {celsius:.3f}ºC')