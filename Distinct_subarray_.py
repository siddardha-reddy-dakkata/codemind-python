n = int(input())
m = int(input())
lst = []
for i in range(n, m + 1):
    lst.append(i)

n = len(lst)
count = 0

for i in lst:
    if i % 2 == 1:
        count += 1

for i in range(n):
    s = lst[i]
    for j in range(i + 1, n):
        s += lst[j]
        if s % 2 == 1:
            count += 1
print(count)