f1 = open('input.txt', 'r')
f2 = open('output.txt', 'w')
l2 = f1.readline(2).strip()
A = list(map(int, f1.readline().split()))
if l2 == '+':
    res = sum(A)
elif l2 == '-':
    res = str(-sum(A)+2*A[0])
elif l2 == '*':
    res = 1
    for i in A:
       res *= i
f2.write(str(res))
f2.close()
f1.close()