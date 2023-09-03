n = int(input())
l = list(map(int,input().split()))

odd = 0
for i in range(n):
    if l[i] % 2 == 1:
        odd += l[i]
print(odd)