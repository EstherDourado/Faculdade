

# Com n é um número inteiro, vamos calcular sua
# quantidade de dígitos, encontrado a primeira
# potência de 10, superior a n.
# Exemplo: 341 - primeira potência de 10 maior: 1000 = 10 ^ 4
# Utilizaremos 4 e não 3 para possibilitar o tratamento de números
# com um só dígito. O ajuste é feito nas fórmulas abaixo

# Solução alternativa, usando apenas inteiros
n = int(input ("Digite o número a verificar:"))
q = 0
while 10 ** q < n:
    q = q + 1
i = q
f = 0
nf = ni = n # Aqui nós copiamos n para ni e nf
pi = pf = 0 # e fazemos pi = pf (para casos especiais)
while i > f:
    pi = int(ni / (10 ** (i-1))) # Dígito mais à direita
    pf = nf % 10                 # Dígito mais à esquerda
    if pi != pf: # Se são diferentes, saímos
        break
    f = f + 1 # Passamos para o próximo dígito a esqueda
    i = i - 1 # Passamos para o dígito a direita seguinte
    ni = ni - (pi * (10 ** i )) # Ajustamos ni de forma a retirar o dígito anterior
    nf = int(nf / 10) # Ajustamos nf para retirar o último dígito

if pi == pf:
    print("%d é palíndromo" % n)
else:
    print("%d não é palíndromo" % n)

