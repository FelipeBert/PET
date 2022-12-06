numPar = 0

for i in range(5):
    num = int(input("Digite um número qualquer: "))
    if num % 2 == 0:
        numPar += 1

print("O usuario digitou {} numeros pares".format(numPar))