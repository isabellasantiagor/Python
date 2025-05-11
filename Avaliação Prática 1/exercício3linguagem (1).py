import math
x_um=int(input('Digite x1 para o ponto P= '))
y_um=int(input('Digite y1 para o ponto P= '))
x_dois=int(input('Digite x2 para o ponto Q= '))
y_dois=int(input('Digite y2 para o ponto Q= '))
distancia=math.sqrt(((x_dois-x_um)**2)+((y_dois-y_um)**2))
print(f'A distância entre os pontos cartesianos é de {distancia:.2f}.')