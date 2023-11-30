row = [0,2,1,3]

loc = {x: i for i, x in enumerate(row)}
ans = 0
for i in range(0, len(row), 2):
    p = row[i]-1 if row[i]%2 else row[i]+1
    if row[i+1] != p:
        ii = loc[p]
        loc[row[i+1]], loc[row[ii]] = loc[row[ii]], loc[row[i+1]]
        row[i+1], row[ii] = row[ii], row[i+1]

print(ans)
