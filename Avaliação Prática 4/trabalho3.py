soma = 0
print("Dobro dos números naturais até 10:")
for i in range(1, 11):
    dobro = i * 2
    print(dobro, end=' ')
    soma += dobro
media = soma / 10
print(f"\nSoma: {soma}")
print(f"Média: {media}")
