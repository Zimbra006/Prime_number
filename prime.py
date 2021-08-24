x = int(input("\nBem vindo ao checador de números primos! Digite um valor para descobrir se é primo:\n"))

maxNum = x + 100
maxCheck = maxNum ** 0.5

primos = []

for i in range(2, maxNum + 1):
    primos += [i]

for num1 in primos:
    if num1 > maxCheck:
        break
    idx = primos.index(num1)
    for num2 in primos[idx + 1:len(primos) + 1]:
        if num2 % num1 == 0:
            primos.remove(num2)
            
def ser_primo(num):
    return num in primos

print(x, ["não é primo\n", "é primo\n"][ser_primo(x)])
