x1 = int(input("Digite o valor de x do primeiro ponto: "))
y1 = int(input("Digite o valor de y do primeiro ponto: "))

def pontos(n_vezes):

    x_i = int(input("Digite o valor de x do ponto seguinte: "))
    y_i = int(input("Digite o valor de y do ponto seguinte: "))
    distancia = ( (x_i - x1)**2 + (y_i - y1)**2 ) ** (1/2)
    print("A distância entre os pontos é de: ", distancia)

    if(n_vezes > 1):
        pontos(n_vezes - 1)


n = int(input("Digite o número de pontos a frente que quer calcular: "))
pontos(n)