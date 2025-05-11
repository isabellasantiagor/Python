inicio = int(input("Digite o valor inicial: "))
contador = 0
print("Sequência decrescente:")
for i in range(inicio, -1, -1):
    print(i, end=' ')
    contador += 1
print(f"\nQuantidade de valores: {contador}")
