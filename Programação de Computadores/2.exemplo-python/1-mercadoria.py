''' 
    Enunciado: Faça um programa solicite o preço de uma mercadoria e o 
    percentual de desconto. Exiba o valor de desconto e o preço a pagar.
'''

valorProduto = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Digite o % de desconto: "))
descontoValor = (valorProduto * desconto)/100
novoValorProduto = valorProduto - descontoValor
print("O valor do desconto foi de: ", descontoValor, " e o novo valor do produto ficou: ",novoValorProduto)