numeros = []
menor = 0
maior = 0
posicaoMenor = 0
posicaoMaior = 0

for i in range(100):
    
    valor = int(input("Digite um valor qualquer: "))
    numeros.append(valor)

    if numeros[i] < menor:
        menor = numeros[i]
        posicaoMenor = i

    elif numeros[i] > maior:
        maior = numeros[i]
        posicaoMaior = i

print("O menor valor foi {} e esta na {} posição".format(menor, posicaoMenor))
print("O maior valor foi {} e esta na {} posição".format(maior, posicaoMaior))