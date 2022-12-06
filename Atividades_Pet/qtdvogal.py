def nvogai(arr):
    vogal = 0
    for i in range(len(arr)):
        if arr[i] == "a" or arr[i] == "A" or arr[i] == "e" or arr[i] == "E" or arr[i] == "i" or arr[i] == "I" or arr[i] == "o" or arr[i] == "O" or arr[i] == "u" or arr[i] == "U":
            vogal += 1
    return vogal

x = ["b", "c", "A", "e", "d", "i"]
y = nvogai(x)
print("O Array apresenta um total de {} vogais".format(y))