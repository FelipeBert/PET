def valorPagamento(valor, dias, pag_total, ncontas):

    pagamento_atual = 0

    if valor == 0:
        print("O número total de prestações foi de {} no total de {} reais".format(ncontas, pag_total))

    elif dias == 0 and valor > 0:

        pagamento_atual = valor
        pag_total += pagamento_atual
        ncontas += 1
        print("Você deve pagar {} reais".format(pagamento_atual))
        n_valor = float(input("Digite o valor da proxima fatura: "))
        n_dias = int(input("Digite os dias de atraso da nova fatura: "))
        valorPagamento(n_valor, n_dias, pag_total, ncontas)

    elif dias > 0 and valor > 0:

        pagamento_atual = valor + (valor * (3/100)) + ((1/100) * dias)
        pag_total += pagamento_atual
        ncontas += 1
        print("Você deve pagar {} reais".format(pagamento_atual))
        n_valor = float(input("Digite o valor da proxima fatura: "))
        n_dias = int(input("Digite os dias de atraso da nova fatura: "))
        valorPagamento(n_valor, n_dias, pag_total, ncontas)

    else:
        if(valor <= 0):
            print("Valor invalido de prestação Tente Novamente!")
            n_valor = int(input("Digite novamente o valor da fatura: "))
            valorPagamento(n_valor, n_dias, pag_total, ncontas)
        else:
            print("Número de dias invalidos Tente novamente!")
            n_dias = int(input("Digite novamente o número de dias: "))
            valorPagamento(valor, n_dias, pag_total, ncontas)

quantia = float(input("Digite o valor da fatura: "))
d_atraso = int(input("Digite a quantidade de dias de atraso: "))

valorPagamento(quantia, d_atraso, 0, 0)