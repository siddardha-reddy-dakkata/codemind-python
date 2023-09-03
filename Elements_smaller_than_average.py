n = int(input())
l = list(map(int,input().split()))

avg = int(sum(l) / n)
c = 0

for i in l:
    if i <= avg:
        c += 1
print(c)