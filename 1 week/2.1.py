n = int(input())
numbers = input()
A = list(map(int, numbers.split()))
cnt = 0
for i in range(n+1):
    cnt = cnt + i
B = sum(A)
print(cnt-B)

