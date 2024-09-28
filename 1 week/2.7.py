A = list(map(int, input().split()))
for i in set(A):
  if A.count(i+1)>A.count(i):
      a = i+1
print(a)