sexo=input('Você é homem ou mulher?')
sexo=sexo.lower()
altura=float(input('Digite sua altura: '))
if sexo =='homem':
    peso_h=(72.7*altura)-58
    print(f'Seu peso ideal é de: {peso_h:.2f}kg.')
elif sexo =='mulher':
    peso_m=(62.1*altura)-44.7
    print(f'Seu peso ideal é de: {peso_m:.2f}kg.')
else:
    print(f'Não existe fórmula para {sexo}')