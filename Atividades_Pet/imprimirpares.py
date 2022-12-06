def pares(num):
    for i in range(len(num)):
        if num[i] % 2 == 0:
            print(num[i])

x = [0, 2, 5, 7, 9, 10, 12]
pares(x)