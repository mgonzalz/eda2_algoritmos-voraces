row = list(map(int, input().split()))
cambios = 0

for i in range(0, len(row), 2):
    if row[i] % 2 == 0: #(0,1), (2,3): (par, impar) -> par + 1 == impar
        a = row[i] + 1
    else:
        a = row[i] - 1
    if row[i + 1] != a:
        cambios += 1
        index = row.index(a)
        row[i + 1], row[index] = row[index], row[i + 1]

print(cambios)
