quantidade=0
soma=0
maiores_que_20=0
print("Digite valores numéricos ou 'fim' para parar):")
while True:
    entrada=input().lower()
    if entrada=='fim':
        break
    valor=float(entrada)
    quantidade+=1
    soma+=valor
    if valor>20:
        maiores_que_20+=1
if quantidade>0:
    media=soma/quantidade
    print("\nResultados:")
    print(f"Quantidade de valores: {quantidade}")
    print(f"Soma dos valores: {soma}")
    print(f"Média dos valores: {media}")
    print(f"Valores acima de 20: {maiores_que_20}")
else:
    print("Nenhum valor foi digitado.")