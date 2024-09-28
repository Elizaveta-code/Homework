A = list(map(int, input().split()))
for i in range(len(A)):
    B = A.count(A[i])
    if B == 1:
        print(A[i])