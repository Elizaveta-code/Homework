A = list(map(int, input().split()))
A.insert(0, A[-1])
A.pop(A[-1])
print(A)
