divida = float(input("Digite o valor da dívida: "))
juros = float(input("Digite a taxa de juros: "))
valormes = float(input("Digite o valor mensal a ser pago: "))

total = (divida * (1 + (juros * 0.01))) 
meses = total / valormes

print ("O valor total da dívida é:", total)
print ("A quantidade de meses a pagar é:", meses)
