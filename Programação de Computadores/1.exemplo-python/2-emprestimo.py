'''
    Enunciado: Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa
    deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação
    mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a
    comprar dividido pelo numero de meses a pagar.
'''

valor_casa = int(input('Valor da casa:'))
salario = int(input('Salário:'))
anos = int(input('Anos a pagar:'))
meses = anos * 12
parcelas = valor_casa / meses
minimo = (salario / 100) * 30

print('')
print('O valor da casa dividido em', meses , 'meses é de:', parcelas,'por mes.')
print('')

if parcelas < minimo:
    print('seu emprestimo foi aprovado.')
else:
    print('seu emprestimo não foi aprovado,pois o valor das parcelas é maior que 30% do seu salário que é de',minimo)