''' 
    Enunciado: Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
    Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45 para viagens mais
    longas.
'''
distancia = float(input('Qual distância você deseja percorrer em km: '))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45

print("O valor da passagem é de: R$", valor)


