final = int(input("Digite o valor final: "))
contador = 0
print("Sequência crescente:")

for i in range(final + 1):
    print(i, end=' ')
    contador += 1
print(f"\nQuantidade de valores: {contador}")
