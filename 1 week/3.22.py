def prost(n, i=2, mn=[]):
    if n <= 1:
        return mn
    elif n % i == 0:
        mn.append(i)
        return prost(n // i, i, mn)
    else:
        return prost(n, i + 1, mn)
num = int(input("Введите число: "))
res = set(prost(num))
print(f"Простые множители числа {num}: {res}")