def produto(num1, num2, num3):

    return num1*num2*num3

def fatorial(num):

    for i in range(num, 1, -1):
        num *= num - 1
    return num

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

fat = int(input("Digite o valor que quer saber do fatorial: "))

x = produto(a, b, c)
y = fatorial(fat)

print("A multiplicação dos produtos da {}".format(x))
print("O fatorial de {} é {}".format(fat, y))