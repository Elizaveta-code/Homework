a = input()
for i in range(1,len(a)//2 + 1):
    if a[i-1] == a[-i]:
        print(f'{a} is a mirrored palindrome.')
for i in range(1,len(a)//2 + 1):
    elif a[i-1] == a[-i]:
        print(f'{a} is a regular palindrome.')
for i in range(1, len(a) // 2 + 1):
    elif a[i-1] == a[-i] or (((a[i-1] == 'E' and a[-i] == '3' or a[i-1] == '3' and a[-i] == 'E')
          or (a[i-1] == 'J' and a[-i] == 'L' or a[i-1] == 'L' and a[-i] == 'J')
          or (a[i-1] == 'Z' and a[-i] == '5' or a[i-1] == '5' and a[-i] == 'Z'))
          or (a[i-1] == 'S' and a[-i] == '2' or a[i-1] == '2' and a[-i] == 'S'))

        print(f'{a} is a mirrored string.')
else:
    print(f'{a} is not a palindrome.')