''' 
    Enunciado: Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa
    deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação
    mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a
    comprar dividido pelo numero de meses a pagar.

    Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
    Pergunte a quantidade de kWh consumida e o tipo de instalação:
        R para residencial,
        I para industrial e
        C para comércios.
        Calcule o preço a pagar de acordo com a tabela a seguir:
	Residencial: Até 500 kWh – R$ 0,40 e acima de 500 kWh – R$ 0,65.
	Comercial: Até 1000 kWh – R$ 0,55 e acima de 1000 kWh – R$ 0,60.
	Industrial: Até 5000 kWh – R$ 0,55 e acima de 5000 kWh – R$ 0,60.

'''

kwh_consumido = int(input('Digite a quantidade de kWh consumida:'))
tipo_instalacao = input('Digite o Tipo de Instalação (R, I ou C):')
tipo_instalacao = tipo_instalacao.upper()
print('')
print('A quantidade de kWh consumido é:', kwh_consumido , 'por mes e o Tipo de Instalação é:', tipo_instalacao)
print('')

if (tipo_instalacao == 'R'):
    if (kwh_consumido <= 500):
        preco_a_pagar = kwh_consumido * 0.40
        print('O valor a pagar pelo consumo de', kwh_consumido,'kWh é de R$',preco_a_pagar,'por mês.')
    else:
        preco_a_pagar = kwh_consumido * 0.65
        print('O valor a pagar pelo consumo de', kwh_consumido,'kWh é de R$',preco_a_pagar,'por mês.')
elif (tipo_instalacao == 'I'):
    if (kwh_consumido <= 1000):
        preco_a_pagar = kwh_consumido * 0.55
        print('O valor a pagar pelo consumo de', kwh_consumido,'kWh é de R$',preco_a_pagar,'por mês.')
    else:
        preco_a_pagar = kwh_consumido * 0.60
        print('O valor a pagar pelo consumo de', kwh_consumido,'kWh é de R$',preco_a_pagar,'por mês.')
elif (tipo_instalacao == 'C'):
    if (kwh_consumido <= 5000):
        preco_a_pagar = kwh_consumido * 0.55
        print('O valor a pagar pelo consumo de', kwh_consumido,'kWh é de R$',preco_a_pagar,'por mês.')
    else:
        preco_a_pagar = kwh_consumido * 0.60
        print('O valor a pagar pelo consumo de', kwh_consumido,'kWh é de R$',preco_a_pagar,'por mês.')
else:
    print("Tipo de Instalação Inválido !")
