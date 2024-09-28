N = int(input())
b = int(input())
c = int(input())
cnt = 0
for i in range(len(str(abs(N)))):
    cnt = cnt + (abs(N) % 10**(i+1)//10**i) * b**i
A = ''
x=abs(cnt)
while x != 0:
    ost = x % c
    x = x // c
    A = A + str(ost)
if N >= 0:
    print(A[::-1])
else:
    print('-'+A[::-1])
