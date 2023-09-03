n = int(input())
l = list(map(int,input().split()))

for i in range(int(n / 2)):
    print(l[i], l[n - i - 1], end = " ")
if n % 2 != 0:
    print(l[int(n / 2)], 0)