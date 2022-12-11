from Banco_Arquivo import Conta, Banco

print("Bem-vindo")
bancoUfrpe = Banco("UABJ")
print("Menu")
print("0 - Sair")
print("1 - Criar uma Nova Conta")
print("2 - Consultar Saldo Conta")
print("3 - Depositar na Conta")
print("4 - Realizar saque")
print("5 - Remover Conta")
escolha = int(input("digite a opção desejada:"))
while escolha > 0:
    if escolha == 1:
        # criar uma conta
        print("Criando Conta...")
        numConta = bancoUfrpe.criarConta()
        print("Conta criada:", numConta)
    elif escolha == 2:
        print("Consultando Saldo...")
        numConta = int(input("digite o numero da conta: "))
        saldo = bancoUfrpe.consultaSaldo(numConta)
        print("o saldo da conta", numConta, "é", saldo, "R$")
    elif escolha == 3:
        print("Depositando Conta...")
        numConta = int(input("digite o numero da conta: "))
        valor = int(input("digite o valor que deseja depositar: "))
        saldo = bancoUfrpe.depositar(numConta, valor)
        print("Valor Depositado")
    elif escolha == 4:
        print("Realizando saque...")
        numConta = int(input("Digite o numero da conta: "))
        valor = int(input("Digite o valor que deseja sacar: "))
        saldo = bancoUfrpe.saque(numConta, valor)
        if saldo == -1:
            print("Saldo Insuficiente!")
        else:
            print("Você realizou um saque de {} reais".format(saldo))
    else:
        numConta = int(input("Digite o numero da conta: "))
        s = bancoUfrpe.remover(numConta)
        if s == 1:
            print("Conta removida com sucesso!")
        else:
            print("Conta não encontrada")
    escolha = int(input("digite a opção desejada:"))