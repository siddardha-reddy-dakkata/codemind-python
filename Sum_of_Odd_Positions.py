n = int(input())
l = list(map(int,input().split()))

odd = 0
for i in range(n):
    if i % 2 != 0:
        odd += l[i]
print(odd)