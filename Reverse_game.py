def reverse(n):
    temp = n
    rev = 0
    while temp != 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    return rev

n = int(input())
l = list(map(int,input().split()))


for i in l:
    print(reverse(i), end = " ")