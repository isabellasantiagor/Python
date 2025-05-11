def somar_tres_valores(a, b, c):
    return a + b + c

def main():
    x = int(input("Digite o primeiro valor: "))
    y = int(input("Digite o segundo valor: "))
    z = int(input("Digite o terceiro valor: "))
    resultado = somar_tres_valores(x, y, z)
    print(f"A soma dos três valores é: {resultado}")
main()
