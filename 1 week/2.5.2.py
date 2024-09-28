A = list(map(int, input().split()))
A = A[-1:] + A[:-1]
print(A)