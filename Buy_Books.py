n = int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

n = sum(l2) - sum(l1)
if n > 0:
    print(n)
else:
    print(0)