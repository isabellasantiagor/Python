def calcula_idade(ano_nascimento):
    ano_atual = 2025
    return ano_atual - ano_nascimento

def main():
    ano = int(input("Digite seu ano de nascimento: "))
    idade = calcula_idade(ano)
    print(f"Sua idade é: {idade} anos")
main()
