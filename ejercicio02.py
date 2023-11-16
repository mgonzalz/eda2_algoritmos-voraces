hunger = list(map(int, input().split()))
n = len(hunger)
suma = n

for i in range(n):
    if i == 0:
        if hunger[i] > hunger[i+1]:
            suma += 1
    elif i == n - 1:
        if hunger[i] > hunger[i-1]:
            suma += 1
    else:
        if hunger[i] > hunger[i+1] or hunger[i] > hunger[i-1]:
            suma += 1

print(suma)
