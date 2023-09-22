n, m = map(int,input().split())
l = []
for i in range(n):
    lst = list(map(int,input().split()))
    l.append(lst)
even = odd = 0

for i in range(n):
    if i % 2 == 0:
        even += sum(l[i])
    else:
        odd += sum(l[i])
print(even, odd)