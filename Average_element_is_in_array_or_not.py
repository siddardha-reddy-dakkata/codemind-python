n = int(input())
l = list(map(int,input().split()))

num = int(sum(l) / n)

print(num in l)