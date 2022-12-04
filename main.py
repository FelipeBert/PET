senha = 2202
tentativa = int(input("Digite a senha: "))

while tentativa != senha:
    print("Senha Incorreta")
    tentativa = int(input("Digite a senha: "))

print("Acesso Permitido!")