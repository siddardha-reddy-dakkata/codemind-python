def is_pal(n):
    temp = n
    rev = 0
    while temp != 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    return rev == n

n = int(input())
l = list(map(int,input().split()))

c = 0
for i in l:
    if is_pal(i):
        c += 1
print(c)