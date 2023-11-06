''' 
    Enunciado: Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
    Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). 
    Exiba o resultado da operação
    solicitada.
'''
num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))
operacao = float(input('(1-Adição) (2-Subtração) (3- Multiplicação) (4- Divisão)'))
if operacao == 1:
    result = num1 + num2
elif operacao == 2:
    result = num1 - num2
elif operacao == 3:
    result = num1 * num2
elif operacao == 4:
    result = num1 / num2
else:
    print ('Opção Invalida')
    result = 0

print("Resultado:",result)