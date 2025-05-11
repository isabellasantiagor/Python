quantidades_impares=0
quantidades_pares=0
soma_pares=0
soma_impares=0
print('Digite 0 para sair.')
while True:
    numero=float(input('Digita um número:'))
    if numero==0:
        break
    if numero%2==0:
        quantidades_pares= quantidades_pares+1
        soma_pares= soma_pares+numero
    else:
        quantidades_impares= quantidades_impares+1
        soma_impares= soma_impares+numero
media_par=soma_pares/quantidades_pares if quantidades_pares>0 else 0
media_impar= soma_impares/quantidades_impares if quantidades_impares>0 else 0
print(f'A média dos números pares é igual à {media_par}')
print(f'A média dos números ímpares é igual à {media_impar}')