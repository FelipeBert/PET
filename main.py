horaInicial = int(input("Digita hora de inicio do jogo: "))
minutoInicial = int(input("Digita minuto de inicio do jogo: "))
horaFinal = int(input("Digita hora de fim do jogo: "))
minutoFinal = int(input("Digita minuto de fim do jogo: "))

tempoHoras = horaFinal - horaInicial
tempoMinutos = minutoFinal - minutoInicial

if(tempoMinutos < 0):
    tempoHoras -= 1
    tempoMinutos = 60 + tempoMinutos

print("O jogo durou {} horas e {} minutos".format(tempoHoras, tempoMinutos))