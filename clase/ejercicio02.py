a = list(map(int, input().split()))
n = len(a)

s = [1]*n
for i in range(n-1):
    if a[i] < a[i+1]:
        s[i+1] += s[i]+1


for i in range(n-1, -1, -1):
    if a[i] > a[i+1]:
        s[i-1] = max(s[i-1], s[i+1] +1)


print(sum(s))

