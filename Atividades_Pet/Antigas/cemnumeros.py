#Considerando que o array ja estive-se com as 100 posições do array preenchidas com dados esta seria uma maneira de determinar o maior e o menor

numeros = []
menor = 0
maior = 0
posicaoMenor = 0
posicaoMaior = 0

for i in range(100):
    if numeros[i] < menor:
        menor = numeros[i]
        posicaoMenor = i

    elif numeros[i] > maior:
        maior = numeros[i]
        posicaoMaior = i

print("O menor valor foi {} e esta na {} posição".format(menor, posicaoMenor))
print("O maior valor foi {} e esta na {} posição".format(maior, posicaoMaior))