x = int(input("Digite um número qualquer: "))
if (x >= 0 and x <= 100):
    print ("X entre 0 e 100")
elif (x > 100 and x < 1000):
    print ("X entre 100 e 1000")
elif (x >= 1000):
    print ("X maior ou igual a 1000")
else:
    print ("X menor que 0")


