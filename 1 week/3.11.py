def fib(n):
    if n <= 0:
        return "Введите число больше нуля"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input("Введите номер числа Фибоначчи: "))
res = fib(n)
print(f"{n}-ое число Фибоначчи: {res}")