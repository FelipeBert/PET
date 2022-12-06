horaInicial = int(input("Digite a hora de inicio do jogo: "))
minutoInicial = int(input("Digite o minuto de inicio do jogo: "))
horaFinal = int(input("Digite a hora de fim do jogo: "))
minutoFinal = int(input("Digite o minuto do fim do jogo: "))

tempoHoras = horaFinal - horaInicial
tempoMinutos = minutoFinal - minutoInicial

if tempoMinutos < 0:
    tempoHoras -= 1
    tempoMinutos = 60 + tempoMinutos

print("O jogo durou {} horas e {} minutos".format(tempoHoras, tempoMinutos))