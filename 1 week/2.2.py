N = int(input())
a = input()
c = ''
for i in range(N):
    j = int(i * (len(a) / N))
    k = int(j+len(a)/N)
    c = c + (a[j:k])[::-1]
print(c)
