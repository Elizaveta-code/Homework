def prost(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            a.append(i)
            n //= i
    if n > 2:
        a.append(n)
    return set(a)
N = int(input("Введите число: "))
result = prost(N)
print(f"Простые множители числа {N}: {result}")