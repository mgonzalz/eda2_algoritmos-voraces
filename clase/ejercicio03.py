array = list(map(int, input().split()))
n = len(array)
m = 0
for i in range(n):
    if i>m:
        return False
    m = max(m, i + array[i])
return True
