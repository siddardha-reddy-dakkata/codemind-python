n, k = map(int,input().split())
lst = list(map(int, input().split()))

count = 0
for i in lst:
    if i == k:
        count += 1
for i in range(n):
    s = lst[i]
    for j in range(i + 1, n):
        s += lst[j]
        if s == k:
            count += 1
print(count)
            