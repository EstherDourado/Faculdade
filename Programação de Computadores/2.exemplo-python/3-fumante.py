''' 
    Enunciado: Escreva um programa para calcular a redução do tempo de vida de um fumante. 
    Pergunte a quantidade de cigarros fumados por dia e quantos anos ela já fumou. 
    Considere que um fumante perde 10 minutos de vida a cada cigarro e calcule 
    quantos dias de vida um fumante perderá. Exiba o total em dias.
'''

cigarros = float(input("Digite a quantidade de cigarros que fuma em um dia:"))
anos = float(input("Digite a quantidade de anos que voce fuma:"))
totalCigarros = cigarros * anos * 365
'''
    Um dia tem 1.440 minutos, se o fumente perde 10 minutos por cigarro, logo, 1.440/10
'''
dias = totalCigarros / 144

print("O total de dias perdidos é: ",dias)
