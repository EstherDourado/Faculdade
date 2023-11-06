q1 = input("Digite a resposta da questão 1: ")
q2 = input("Digite a resposta da questão 2: ")
q3 = input("Digite a resposta da questão 3: ")

pont = 0

if (q1 == 'b' or q1 == 'B'):
    pont = pont + 1
if (q2 == 'a' or q2 == 'A'):
    pont = pont + 1
if (q3 == 'd' or q3 == 'D'):
    pont = pont + 1

print("A quantidade de acertos é: ", pont)
