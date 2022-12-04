idadeSoma = 0
idade = []
idadeNegativa = 1

while idadeNegativa != 0:
    x = int(input("Digite sua idade: "))
    if x < 0:
        idadeNegativa = 0
    else:
        idade.append(x)
        idadeSoma += x

print("A média das idades foi: {}".format(idadeSoma / len(idade)))