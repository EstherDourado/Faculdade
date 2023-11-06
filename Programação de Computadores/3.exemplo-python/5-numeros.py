numero = int (input("Digite um número inteiro: "))
total = 0
contador = 0

while (numero != 0):
    total = total + numero
    contador = contador + 1
    numero = int (input("Digite um número inteiro: "))

med = total / contador
print("A quantidade de numeros digitados é: ", contador, "a soma deles é: ", total, "e a média é: ", med)
