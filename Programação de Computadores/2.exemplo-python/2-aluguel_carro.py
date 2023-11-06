''' 
    Enunciado: Escreva um programa que pergunte a quantidade de km percorridos 
    por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais 
    o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia 
    e R$ 0,15 por km rodado.
'''

km = float(input("Digite a quantidade de km rodados: "))
dias = float(input("Digite a quantidade de dias da locação: "))
valor = (0.15 * km) + (60 * dias)
print("O valor da locação é de: R$ ",valor)