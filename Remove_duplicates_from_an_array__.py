n = int(input())
l = list(map(int,input().split()))

l = list(set(l))
l.sort()
print(*l)