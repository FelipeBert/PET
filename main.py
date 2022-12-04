vitorias = int(input("Indique o número de vitorias que a equipe teve: "))
empates = int(input("Indique o número de empates que a equipe teve: "))
derrotas = int(input("Indique o número de derrotas que a equipe teve: "))

vitorias = vitorias * 3
pontos = vitorias + empates
print("Você teve {} pontos".format(pontos))