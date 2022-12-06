idadeNegativa = 0
idadeSoma = 0
idade = []

while idadeNegativa != 1:
    idadePositiva = int(input("Digite sua Idade: "))
    if idadePositiva < 0:
        idadeNegativa = 1
    else:
        idadeSoma += idadePositiva
        idade.append(idadePositiva)

if idadeSoma == 0:
    print("Nenhuma idade valida foi inserida no programa")
else:
    print("A idade média dos usuarios foi de {}".format(idadeSoma / len(idade)))