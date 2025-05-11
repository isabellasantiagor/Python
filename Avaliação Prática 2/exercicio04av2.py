a=float(input('Digite o primeiro valor:'))
b=float(input('Digite o segundo valor:'))
operacao=(input('Digite a operação desejada entre +,-,* ou /:'))
if operacao == '+':
    soma=a+b
    print(f'O resultado é {soma}')
elif operacao == '-':
        subtracao=a-b
        print(f'O resultado é {subtracao}')
elif operacao == '*':
        multiplicacao=a*b
        print(f'O resultado é {multiplicacao}')
elif operacao == '/':
        if b==0:
            print('Não é possível dividir por 0!')
        else:
             divisao=a/b
             print(f'O resultado é {divisao}')
else:
    print('Operação desejada inválida.')