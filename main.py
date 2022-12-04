numPar = 0

for i in range(5):
    valor = int(input("Digite um valor: "))
    if valor % 2 == 0:
        numPar += 1

print("Usuario digitou {} numeros pares".format(numPar))