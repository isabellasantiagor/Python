soma = 0
print("Múltiplos de 3 até 21:")
for i in range(3, 22, 3):
    print(i, end=' ')
    soma += i
print(f"\nSoma dos números: {soma}")
