f1 = open('input.txt', 'r')
f2 = open('output.txt', 'w')
l2 = f1.readline(2).split()
l3 = int(f1.readline(3))
S = list(map(int, f1.readline().split()))
cnt0 = 0
for i in range(len(S)):
    for k in range(len(str(S[i]))):
        cnt0 = cnt0 + (S[i] % 10**(k+1)//10**k) * l3**k
cnt1=1
for y in range(len(S)):
    cnt11 = 0
    for z in range(len(str(S[y]))):
        cnt11 = cnt11 + (S[y] % 10**(z+1)//10**z) * l3**z
    cnt1 = cnt11 * cnt1
first = 0
for p in range(len(str(S[0]))):
    first = first + (S[0] % 10 ** (p + 1) // 10 ** p) * l3 ** p
cnt2 = first*2-cnt0
summa = ''
a = abs(cnt0)
while a != 0:
    ost0 = a % l3
    a = a//l3
    summa = summa + str(ost0)
A = summa[::-1]
if cnt0 >= 0:
    A=A
else:
    A='-'+A
mul = ''
b = abs(cnt1)
while b != 0:
    ost1 = b % l3
    b = b//l3
    mul = mul + str(ost1)
B = mul[::-1]
if cnt1 >= 0:
    B=B
else:
    B='-'+B
razn = ''
c = abs(cnt2)
while c != 0:
    ost2 = c % l3
    c = c//l3
    razn = razn + str(ost2)
C = razn[::-1]
if cnt2 >= 0:
    C=C
else:
    C='-'+C
l2 = l2[0]
if l2 == '-':
    n = C
elif l2 == '*':
    n = B
else:
    n = A
f2.write(n)
f2.close()
f1.close()
