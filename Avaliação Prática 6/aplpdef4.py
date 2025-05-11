def calcular_salario(horas_trabalhadas, valor_hora):
    return horas_trabalhadas * valor_hora

def main():
    horas = float(input("Digite a quantidade de horas trabalhadas: "))
    valor = float(input("Digite o valor da hora trabalhada: "))
    salario = calcular_salario(horas, valor)
    print(f"Salário bruto: R${salario:.2f}")
main()
