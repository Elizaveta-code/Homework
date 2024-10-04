def solve(N, M, matrix):
    for i in range(N):
        for j in range(N):
            if i != j:
                kf = matrix[j][i] / matrix[i][i]
                for k in range(M):
                    matrix[j][k] -= kf * matrix[i][k]
    res = [0] * N
    for i in range(N):
        res[i] = matrix[i][M - 1] / matrix[i][i]
    return res
N = int(input("Введите количество строк: "))
M = int(input("Введите количество столбцов: "))
matrix = []
for i in range(N):
    A = list(map(float, input().split()))
    matrix.append(A)
solution = solve(N, M, matrix)
print("Решение системы уравнений:")
for i in range(N):
    print(f"x{i + 1} = {solution[i]}")