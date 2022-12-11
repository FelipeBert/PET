horaSaida = int(input("Digite a hora de saida: "))
tempoViagem = int(input("Digite o tempo que a viagem durou: "))
fuso = int(input("Digite o fuso do local: "))

horario = horaSaida + tempoViagem + fuso
if horario < 0:
    horario = 24 + horario
elif horario > 23:
    diferença = horario - 24
    horario = 0 + diferença

print("Você ira ao local as {}".format(horario))