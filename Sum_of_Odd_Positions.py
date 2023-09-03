n = int(input())
l = list(map(int,input().split()))

even = odd = 0
for i in range(n):
    if i % 2 == 0:
        even += l[i]
    else:
        odd += l[i]
print(abs(even - odd))