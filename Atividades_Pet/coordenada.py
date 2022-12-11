def pontos():
    x1 = int(input("Digite o valor de x do primeiro ponto: "))
    y1 = int(input("Digite o valor de y do primeiro ponto: "))

    for i in range(5):
        x_i = int(input("Digite o valor de x do ponto seguinte: "))
        y_i = int(input("Digite o valor de y do ponto seguinte: "))
        distancia = ( (x_i - x1)**2 + (y_i - y1)**2 ) ** (1/2)
        print("A distância entre os pontos é de: ", distancia)


pontos()