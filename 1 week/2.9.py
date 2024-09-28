f = open('input2.txt', 'r')
r = f.read()
A = list(r.split())
cnt = 0
for i in range(len(A)):
    if '.' in A[i] or '!' in A[i] or '?' in A[i]:
        cnt = cnt + 1
print(cnt)