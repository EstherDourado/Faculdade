tab = int(input("Digite o numero da tabuada: ")) 
inicio = int(input("Digite o numero de inicio da tabuada: ")) 
fim = int(input("Digite o numero do fim da tabuada: ")) 

while inicio <= fim:
    print(tab," X ", inicio, " = ", tab * inicio)
    inicio = inicio + 1
