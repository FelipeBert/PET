def liquido(salario):
    inss = (11/100) * salario
    ir = (15/100) * (salario - inss)
    print("O seu salário liquido é de {}".format(salario - (inss + ir)))

bruto = int(input("Digite seu salário Bruto: "))
liquido(bruto)