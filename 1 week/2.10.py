f = open('input3.txt', 'r', encoding="utf-8")
a = f.read()
A=a
c = ['б', 'в', 'г', 'л', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
g = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
for i in range(1, len(A)):
    if ((A[i-1] in c) or (A[i-1] == ' ')) and (A[i] in g) and ((A[i+1] in c) or (A[i+1] == ' ')):
        A = A.replace(A[i], A[i] + 'c' + A[i])
print(A)